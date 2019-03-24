#include "ObjDetection.h"

using namespace cv;
using namespace dnn;
using namespace std;

ObjDetection::ObjDetection() :
	m_ipImage(this, &ObjDetection::callback, "image_in"),
	m_opImage(this, "image_seg"),
	m_opData(this, "out")
{
	m_ipImage.getPort<0>().addImageType(cImgType::RGB32, 4);
	net = loadYOLOv3(classes);
}

ObjDetection::~ObjDetection()
{

}

cImg function(cImg Image)
{
	return Image;
	//function definition for the segmentation
}

void ObjDetection::callback(cBufferT<cImg> *i_buffer)
{
	cImg srcImage = i_buffer->getData();
	QImage tempsrc = srcImage.toQImage().convertToFormat(QImage::Format_RGB888);
	Mat srcImageMat(tempsrc.height(), tempsrc.width(), CV_8UC3, tempsrc.bits(), tempsrc.bytesPerLine());
	vector<Rect> boundingBoxes;
	detectWrapper(net, srcImageMat, classes, boundingBoxes);
	QImage imgIn((uchar*)srcImageMat.data, srcImageMat.cols, srcImageMat.rows, srcImageMat.step, QImage::Format_RGB888);
	cImg dstImage;
	dstImage = cImg::fromQImage(imgIn);
	c2DPoint<float64> centerPoint(boundingBoxes.at(0).x + boundingBoxes.at(0).width / 2, boundingBoxes.at(0).y + boundingBoxes.at(0).height / 2);
	veData sensorData("sensor1", i_buffer->getStamp().getStamp());
	veCameraPixelCoordinate boxPix(centerPoint, sensorData);
	c3DPoint<float64> out;
	veCalibration s; s.measurementToWorld(&boxPix, out);
	m_opImage.send(dstImage, m_ipImage.getStamp()); //sending the segmented image to output port
	m_opData.send(out, i_buffer->getStamp());
}



STATION(ObjDetection, "camera/ObjDetection");