#pragma once

#include "cdl/cStation.h"
#include "cbl/cMathOP.h"
#include "cil/cImgConvertFunctor.h"
#include "cil/cMinMaxFunctor.h"
#include "cil/cImgMirrorFunctor.h"
#include "cvw/cMainWindow.h"
#include <QPainter>
#include <QPaintEngine>
#include "cil/cImg.h"

class Segmentation : public cStation
{
	STATIONDECL(Segmentation);
	Segmentation();
	virtual ~Segmentation();
	void callback(cBufferT<cImg> *i_buffer);
	//	virtual void initialize(const cMapObj &i_params);
	//	virtual void start(StartReasons i_reasons);
	//	virtual void stop(StopReasons i_reason);
	//	virtual void destroy();
	//	virtual void enabled(bool i_on);

	PORT(cImg) m_ipImage;
	cOPort<cImg> m_opImage;
	cOPort<cDblRange> m_opRange;
};