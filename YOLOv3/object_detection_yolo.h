#include <fstream>
#include <sstream>
#include <iostream>
#include <opencv2/dnn.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace dnn;
using namespace std;

// Load the names of classes and the network
Net loadYOLOv3(vector<string>& classes);

// Processing a frame
void detect(Net& net, Mat& frame, vector<string>& classes, VideoWriter& video);

// Remove the bounding boxes with low confidence using non-maxima suppression
void postprocess(Mat& frame, vector<string>& classes, const vector<Mat>& out);

// Draw the predicted bounding box
void drawPred(int classId, vector<string>& classes, float conf, int left, int top, int right, int bottom, Mat& frame);

// Get the names of the output layers
vector<String> getOutputsNames(const Net& net);