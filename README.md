# about 

- use mmengine to train on kitti dataset 

# prepare dataset 

- kitti-tiny can be obtained from https://github.com/open-mmlab/OpenMMLabCourse/tree/main/codes/MMDet3d_tutorials or https://github.com/open-mmlab/mmdetection/blob/master/demo/MMDet_Tutorial.ipynb

- python tools/create_data.py kitti --root-path ./data/kitti --out-dir ./data/kitti --extra-tag kitti