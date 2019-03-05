#include "Segmentation.h"

Segmentation::Segmentation() :
	m_ipImage(this, &Segmentation::callback, "image_in"),
	m_opRange(this, "range"),
	m_opImage(this, "image_seg")
{
	m_ipImage.getPort<0>().addImageType(cImgType::RGB32, 4);
}

Segmentation::~Segmentation()
{

}

cImg function(cImg Image)
{
	return Image;
	//function definition for the segmentation
}

void Segmentation::callback(cBufferT<cImg> *i_buffer)
{
	cImg srcImage = i_buffer->getData();
	cImg dstImage = function (srcImage);
	cDblRange range;
	uint8 min = 0;
	uint8 max = 255;
	range = cDblRange(min, max);
	m_opImage.send(dstImage, m_ipImage.getStamp()); //sending the segmented image to output port
	m_opRange.send(range, i_buffer->getStamp()); //sending the range to output range port
}



//not really sure how to write the function definition for finding the range !!


STATION(Segmentation, "camera/Segmentation");