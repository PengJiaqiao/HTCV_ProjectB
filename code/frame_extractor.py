import os
import sys

import skvideo
import skvideo.io

from PIL import Image

def frame_extractor(path_to_video, output_dir, save_every=100):
    capture = skvideo.io.vreader(path_to_video)
    cur_frame = 0
    while True:      
        try:
            frame = next(capture)
        except StopIteration:
            return
        else:
            if cur_frame % save_every == 0:
                name = 'frame_{:05d}.jpg'.format(cur_frame)
                result = Image.fromarray(frame)
                result.save(os.path.join(output_dir, name))
            cur_frame+=1

def main():
    if len(sys.argv) >= 3: 
        video_dir = sys.argv[1]
        output_dir = sys.argv[2]
        save_every = 100
        if len(sys.argv) == 4:
            save_every = int(sys.argv[3])

        video_paths = [
            os.path.join(video_dir, file) for file in os.listdir(sys.argv[1]) if os.path.splitext(file)[1] in ('.avi')]

        for video_path in video_paths:
            filename_no_ext = os.path.splitext(os.path.basename(video_path))[0]
            cur_video_output_dir = os.path.join(output_dir, filename_no_ext) 
            if not os.path.exists(cur_video_output_dir):
                os.makedirs(cur_video_output_dir)

            frame_extractor(video_path, cur_video_output_dir, save_every)
    else: 
        raise ValueError("Bad format. Expected <file>.py <path to video directory> <output directory> [<save every>]")

if __name__ == "__main__":
    main()