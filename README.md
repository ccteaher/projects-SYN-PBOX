# SYN-PBOX: A Large Scale Benchmark Dataset for 3D Box-shaped Object Recognition in Scene Understanding of Bin Picking

![the emample of SYN-PBOX](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/example/SYN-PBOX.gif)

# Download Dataset
## SYN-PBOX_v2
You can download the synthetic dataset (SYN-PBOX) from Link(https://pan.baidu.com/s/1mgVtO9FHG-BFoWgxMdCOcg code:8qla). Unzip and save in ./dataset/.
## SYN-PBOX_v1
You can download the real world dataset (Real-PBOX) set from Link(https://pan.baidu.com/s/1n4dX-3Y_k7Qlg4njU_leoQ code:umph). Unzip and save in ./dataset.

# SYN-PBOX - Supplemental Video
[![Watch the video](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/video/Supplemental.png)](https://www.youtube.com/watch?v=tk9xEbmGMGg)

# Models
You can download the models from Link(https://pan.baidu.com/s/1bVI2WHTHcJisZpFIRSyzCQ code:l8rw). 

We advise to use meshlab for viewing the .obj meshes or the .ply files.

# Dataset Structure
The dataset have the following structure:
    
    DATASET_NAME
    DATA
    ├─ single
    │  ├─ obj_OBJ_ID
    │  │  ├─ OBJ_ID_bop_data
    │  │  │  ├─ train|val|test[_TYPE]
    │  │  │  │  ├─ scene_camera.json
    │  │  │  │  ├─ scene_gt.json
    │  │  │  │  ├─ scene_gt_info.json
    │  │  │  │  ├─ depth
    │  │  │  │  ├─ mask
    │  │  │  │  ├─ mask_visib
    │  │  │  │  ├─ rgb|gray
    │  │  │  ├─ camera[_TYPE].json
    │  │  ...
    │  ...
    ├─ multiple
    │  ├─ OBJ_ID_bop_data
    │  │  ├─ train|val|test[_TYPE]
    │  │  │  ├─ scene_camera.json
    │  │  │  ├─ scene_gt.json
    │  │  │  ├─ scene_gt_info.json
    │  │  │  ├─ depth
    │  │  │  ├─ mask
    │  │  │  ├─ mask_visib
    │  │  │  ├─ rgb|gray
    │  │  ├─ camera[_TYPE].json
    │  ...

    MODELS
    ├─ camera[_TYPE].json
    ├─ models[_MODELTYPE][_eval]
    │  ├─ obj_OBJ_ID.png
    │  ├─ obj_OBJ_ID.mtl
    │  ├─ obj_OBJ_ID.obj
    │  ├─ obj_OBJ_ID.ply
    │  ...




# SYN-PBOX Image
![the emample of SYN-PBOX](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/example/images/fig1.png)

# Objects
![the emample of SYN-PBOX](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/example/images/fig2.png)
