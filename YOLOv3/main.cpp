#include <fstream>
#include <sstream>
#include <iostream>
#include <opencv2/dnn.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include "object_detection_yolo.h"

// Usage example:  ./object_detection_yolo.out --video=PMD_Example_left.avi
const char* keys = 
"{help h usage ? | | Usage examples: ./object_detection_yolo.out --video=PMD_Example_left.avi}"
"{video v       |<none>| input video   }"
;

using namespace cv;
using namespace dnn;
using namespace std;

int main(int argc, char** argv) {
    CommandLineParser parser(argc, argv, keys);
    // Load the classes name and the network
    vector<string> classes;
    Net net = loadYOLOv3(classes); // Put this into Cassandra station constructor
    
    // Open a video file
    string str, outputFile;
    VideoCapture cap;
    VideoWriter video;
    Mat frame;

    str = parser.get<String>("video");
    ifstream ifile(str.c_str());
    if(!ifile) throw("error");
    cap.open(str.c_str());
    str.replace(str.end()-4, str.end(), "_yolo_out_cpp.avi");
    outputFile = str;

    // Get the video writer initialized to save the output video
    video.open(outputFile, VideoWriter::fourcc('M','J','P','G'), 28, Size(cap.get(CAP_PROP_FRAME_WIDTH), cap.get(CAP_PROP_FRAME_HEIGHT)));
    
    // Create a window
    static const string kWinName = "Deep learning object detection in OpenCV";
    namedWindow(kWinName, WINDOW_NORMAL);

    // Process each frame.
    while (waitKey(1) < 0)
    {
        // get frame from the video
        cap >> frame;

        // Stop the program if reached end of video
        if (frame.empty()) {
            cout << "Done processing" << endl;
            waitKey(3000);
            break;
        }

        // Process a frame
        detect(net, frame, classes, video); // Put this into Cassandra callback function
        imshow(kWinName, frame);
    }

    cap.release();
    video.release();

    return 0;
}