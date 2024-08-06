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
│   ├── metadata_cameras.csv                     # list of all the camera trajectories for this scene
│   ├── metadata_node_strings.csv                # all human-readable strings in the definition of each V-Ray node
│   ├── metadata_nodes.csv                       # establishes a correspondence between the object names in an exported OBJ file, and the V-Ray node IDs that are stored in our render_entity_id images
│   ├── metadata_scene.csv                       # includes the scale factor to convert asset units into meters
│   ├── cam_XX                                   # camera trajectory information
│   │   ├── camera_keyframe_orientations.hdf5    # camera orientations
│   │   └── camera_keyframe_positions.hdf5       # camera positions (in asset coordinates)
│   ├── ...
│   └── mesh                                                                            # mesh information
│       ├── mesh_objects_si.hdf5                                                        # NYU40 semantic label for each object ID (available in our public code repository)
│       ├── mesh_objects_sii.hdf5                                                       # semantic instance ID for each object ID (available in our public code repository)
│       ├── metadata_objects.csv                                                        # object name for each object ID (available in our public code repository)
│       ├── metadata_scene_annotation_tool.log                                          # log of the time spent annotating each scene (available in our public code repository)
│       ├── metadata_semantic_instance_bounding_box_object_aligned_2d_extents.hdf5      # length (in asset units) of each dimension of the 3D bounding for each semantic instance ID
│       ├── metadata_semantic_instance_bounding_box_object_aligned_2d_orientations.hdf5 # orientation of the 3D bounding box for each semantic instance ID
│       └── metadata_semantic_instance_bounding_box_object_aligned_2d_positions.hdf5    # position (in asset coordinates) of the 3D bounding box for each semantic instance ID
└── images
    ├── scene_cam_XX_final_hdf5                  # lossless HDR image data that requires accurate shading
    │   ├── frame.IIII.color.hdf5                # color image before any tone mapping has been applied
    │   ├── frame.IIII.diffuse_illumination.hdf5 # diffuse illumination
    │   ├── frame.IIII.diffuse_reflectance.hdf5  # diffuse reflectance (many authors refer to this modality as "albedo")
    │   ├── frame.IIII.residual.hdf5             # non-diffuse residual
    │   └── ...
    ├── scene_cam_XX_final_preview               # preview images
    |   └── ...
    ├── scene_cam_XX_geometry_hdf5               # lossless HDR image data that does not require accurate shading
    │   ├── frame.IIII.depth_meters.hdf5         # Euclidean distances (in meters) to the optical center of the camera
    │   ├── frame.IIII.position.hdf5             # world-space positions (in asset coordinates)
    │   ├── frame.IIII.normal_cam.hdf5           # surface normals in camera-space (ignores bump mapping)
    │   ├── frame.IIII.normal_world.hdf5         # surface normals in world-space (ignores bump mapping)
    │   ├── frame.IIII.normal_bump_cam.hdf5      # surface normals in camera-space (takes bump mapping into account)
    │   ├── frame.IIII.normal_bump_world.hdf5    # surface normals in world-space (takes bump mapping into account)
    │   ├── frame.IIII.render_entity_id.hdf5     # fine-grained segmentation where each V-Ray node has a unique ID
    │   ├── frame.IIII.semantic.hdf5             # NYU40 semantic labels
    │   ├── frame.IIII.semantic_instance.hdf5    # semantic instance IDs
    │   ├── frame.IIII.tex_coord.hdf5            # texture coordinates
    │   └── ...
    ├── scene_cam_XX_geometry_preview            # preview images
    |   └── ...
    └── ...


# SYN-PBOX Image


# Objects

