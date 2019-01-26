import os
import io
import sys
import json
import argparse
from bs4 import BeautifulSoup
import tensorflow as tf

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, 'models', 'research'))

from object_detection.utils import dataset_util
from object_detection.utils import label_map_util

def is_valid_bbox(bbox):
	"""Check if the bounding box is valid

	Args:
		bbox - A tuple (xmin, ymin, xmax, ymax)
	"""
	xmin, ymin, xmax, ymax = bbox
	if xmin < 0 or xmin > xmax or xmax > 1 or \
	   ymin < 0 or ymin > ymax or ymax > 1:
	   return False
	return True

class TFRecordBuilder():
	def __init__(self, images_dir, labels_dir, label_map_file, output_file):
		self.image_format = b'jpeg'
		self.images_dir = images_dir
		self.labels_dir = labels_dir
		self.label_map_dict = label_map_util.get_label_map_dict(label_map_file)
		self.output_file = output_file
		self.all_labels = [file for file in os.listdir(self.labels_dir) if os.path.splitext(file)[1] in '.xml']

		if len(self.all_labels) == 0:
			raise ValueError('No labels found in: {}'.format(labels_dir))

		with open(os.path.join(labels_dir, self.all_labels[0])) as f:
			xml_file = BeautifulSoup(f, 'xml')

		self.width = int(xml_file.size.width.text)
		self.height = int(xml_file.size.height.text)

	def _extract_detections(self, label_file):
		output = dict(class_names=[], bboxes=[])

		detections = label_file.find_all('object') 
		for detection in detections:
			class_name = str(detection.find('name', recursive=False).text)

			bndbox = detection.find('bndbox', recursive=False)

			xmin_norm = float(bndbox.xmin.text) / self.width
			ymin_norm = float(bndbox.ymin.text) / self.height
			xmax_norm = float(bndbox.xmax.text) / self.width
			ymax_norm = float(bndbox.ymax.text) / self.height

			bbox = (xmin_norm, ymin_norm, xmax_norm, ymax_norm)
			if class_name not in self.label_map_dict or \
				not is_valid_bbox(bbox):
				continue

			output['class_names'].append(class_name.encode("utf8"))
			output['bboxes'].append(bbox)

		return output

	def _build_intermediate(self):
		preprocessed_labels = []

		for xml_file in self.all_labels:
			with open(os.path.join(self.labels_dir, xml_file)) as f:
				xml_file_soup = BeautifulSoup(f, 'xml')
				
			current = dict()

			detections = self._extract_detections(xml_file_soup)

			current['filename'] = (os.path.splitext(xml_file)[0] + '.jpg').encode('utf-8')
			current['width'] = self.width
			current['height'] = self.height
			current['class_names'] = detections['class_names']
			current['classes'] = [self.label_map_dict[elem] for elem in detections['class_names']]

			current['xmin'] = [elem for elem in detections['bboxes'][0]]
			current['xmax'] = [elem for elem in detections['bboxes'][1]]
			current['ymin'] = [elem for elem in detections['bboxes'][2]]
			current['ymax'] = [elem for elem in detections['bboxes'][3]]

			with tf.gfile.GFile(os.path.join(self.images_dir, current['filename']), 'rb') as fid:
				current['encoded'] = fid.read()

			preprocessed_labels.append(current)

		return preprocessed_labels

	def _generate_single_record(self, preprocessed_label):
		tf_record = tf.train.Example(features=tf.train.Features(feature={
			'image/height': dataset_util.int64_feature(self.height),
			'image/width': dataset_util.int64_feature(self.width),
			'image/filename': dataset_util.bytes_feature(preprocessed_label['filename']),
			'image/source_id': dataset_util.bytes_feature(preprocessed_label['filename']),
			'image/encoded': dataset_util.bytes_feature(preprocessed_label['encoded']),
			'image/format': dataset_util.bytes_feature(self.image_format),
			'image/object/bbox/xmin': dataset_util.float_list_feature(preprocessed_label['xmin']),
			'image/object/bbox/xmax': dataset_util.float_list_feature(preprocessed_label['xmax']),
			'image/object/bbox/ymin': dataset_util.float_list_feature(preprocessed_label['ymin']),
			'image/object/bbox/ymax': dataset_util.float_list_feature(preprocessed_label['ymax']),
			'image/object/class/text': dataset_util.bytes_list_feature(preprocessed_label['class_names']),
			'image/object/class/label': dataset_util.int64_list_feature(preprocessed_label['classes']),
		}))
		return tf_record


	def build(self):
		writer = tf.python_io.TFRecordWriter(self.output_file)
		
		for elem in self._build_intermediate():
			record = self._generate_single_record(elem)
			writer.write(record.SerializeToString())

		writer.close()

def main():
	parser = argparse.ArgumentParser()
	requiredNamed = parser.add_argument_group('required named arguments')
	requiredNamed.add_argument('-id', '--image_dir', help="The directory that contains the images.", required=True)
	requiredNamed.add_argument('-ld', '--label_dir', help="The directory that contains the labels.", required=True)
	requiredNamed.add_argument('-l', '--label_map', help="The path to a label map file.", required=True)
	requiredNamed.add_argument('-o', '--output', help="Name of the file, where data will be stored.", required=True)

	args = parser.parse_args()

	if not os.path.isdir(args.image_dir):
		raise ValueError('No such directory: {}'.format(args.image_dir))
	
	if not os.path.isdir(args.label_dir):
		raise ValueError('No such directory: {}'.format(args.label_dir))

	if not os.path.isfile(args.label_map):
		raise ValueError('No such file: {}'.format(args.label_map))

	TFRecordBuilder(args.image_dir, args.label_dir, args.label_map, args.output).build()

if __name__ == '__main__':
	main()
