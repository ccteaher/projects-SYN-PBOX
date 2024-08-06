# SYN-PBOX: A Large Scale Benchmark Dataset for 3D Box-shaped Object Recognition in Scene Understanding of Bin Picking

![the emample of SYN-PBOX](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/example/SYN-PBOX.gif)

# Download Dataset
## SYN-PBOX_v2
You can download the synthetic dataset (SYN-PBOX) from Link(https://pan.baidu.com/s/1vHxTObDSviUlTk--F7e43A code:efcv). Unzip and save in ./dataset/.
## SYN-PBOX_v1
You can download the real world dataset (Real-PBOX) set from Link(https://pan.baidu.com/s/1vHxTObDSviUlTk--F7e43A code:efcv). Unzip and save in ./dataset.

# SYN-PBOX - Supplemental Video
[![Watch the video](https://github.com/ccteaher/projects-SYN-PBOX/blob/main/video/Supplemental.png)](https://www.youtube.com/watch?v=tk9xEbmGMGg)

# Dataset Structure

    ai_VVV_NNN
    ├── _detail
    │   ├── metadata_cameras.csv                     
    │   ├── metadata_node_strings.csv                
    │   ├── metadata_nodes.csv                      
    │   ├── metadata_scene.csv                       
    │   ├── cam_XX                                   
    │   │   ├── camera_keyframe_orientations.hdf5   
    │   │   └── camera_keyframe_positions.hdf5       
    │   ├── ...
    │   └── mesh                                                                           
    │       ├── mesh_objects_si.hdf5                                                       
    │       ├── mesh_objects_sii.hdf5                                                       
    │       ├── metadata_objects.csv                                                       
    │       ├── metadata_scene_annotation_tool.log                                          
    │       ├── metadata_semantic_instance_bounding_box_object_aligned_2d_extents.hdf5      
    │       ├── metadata_semantic_instance_bounding_box_object_aligned_2d_orientations.hdf5 
    │       └── metadata_semantic_instance_bounding_box_object_aligned_2d_positions.hdf5    
    └── images
        ├── scene_cam_XX_final_hdf5                  
        │   ├── frame.IIII.color.hdf5               
        │   ├── frame.IIII.diffuse_illumination.hdf5 
        │   ├── frame.IIII.diffuse_reflectance.hdf5  
        │   ├── frame.IIII.residual.hdf5             
        │   └── ...
        ├── scene_cam_XX_final_preview               
        |   └── ...
        ├── scene_cam_XX_geometry_hdf5               
        │   ├── frame.IIII.depth_meters.hdf5         
        │   ├── frame.IIII.position.hdf5             
        │   ├── frame.IIII.normal_cam.hdf5           
        │   ├── frame.IIII.normal_world.hdf5         
        │   ├── frame.IIII.normal_bump_cam.hdf5      
        │   ├── frame.IIII.tex_coord.hdf5            
        │   └── ...
        ├── scene_cam_XX_geometry_preview            
        |   └── ...
        └── ...


# SYN-PBOX Image


# Objects

