import blenderproc as bproc
import argparse
import numpy as np
import bpy
import os
import random
import time
from mathutils import Vector, Matrix
from math import acos
import math


parser = argparse.ArgumentParser()

parser.add_argument('LBox_blend_model', nargs='?', default="hello/scene_model/wooden_table_02_1k.blend",
                    help="Path to the object file with the LBox object")

parser.add_argument('output_dir', nargs='?', default="hello/train_bop_output2",
                    help="Path to where the final files, will be saved")

parser.add_argument('bop_parent_path', help="Path to the bop datasets parent directory")
args = parser.parse_args()


bproc.init()

##  Only Use GPU ####################################################################################
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.preferences.addons["cycles"].preferences.get_devices()
for d in bpy.context.preferences.addons["cycles"].preferences.devices:
    # only use GPU.
    if d["name"] == '':
        d["use"] = 0
    else:
        d["use"] = 1
    print(d["name"], d["use"])
###############################################################################################


rand_num = np.random.randint(1, 9)
object_number = rand_num


target_bop_objs = []

for i in range(object_number):
    target_bop_objs += bproc.loader.load_bop_PlyToObjs_single(bop_dataset_path=os.path.join(args.bop_parent_path, 'ourssix'),
                                                              obj_ids=[1], single_object=True, object_number=i)


# icbin_dist_bop_objs = bproc.loader.load_bop_objs(bop_dataset_path=os.path.join(args.bop_parent_path, 'icbin'), mm2m=True)
# ycbv_dist_bop_objs = bproc.loader.load_bop_objs(bop_dataset_path=os.path.join(args.bop_parent_path, 'ycbv'), mm2m=True)
# hb_dist_bop_objs = bproc.loader.load_bop_objs(bop_dataset_path=os.path.join(args.bop_parent_path, 'hb'), mm2m=True)


# for i in range(object_number):
#     print(target_bop_objs[i].__dict__)
#     print(target_bop_objs[i].blender_obj)
#     lefuqiu=target_bop_objs[i].blender_obj
#     print(lefuqiu.name)


bproc.loader.load_bop_intrinsics(bop_dataset_path=os.path.join(args.bop_parent_path, 'ourssix'))


# for obj in (target_bop_objs + icbin_dist_bop_objs + ycbv_dist_bop_objs + hb_dist_bop_objs):
for obj in (target_bop_objs):
    obj.set_shading_mode('auto')
    obj.hide(True)

# ##### load ##########################################################################################
LBox_blend = bproc.loader.load_blend(args.LBox_blend_model)
LBox = bproc.filter.one_by_attr(LBox_blend, "name", "Cube")


light_plane = bproc.object.create_primitive('PLANE', scale=[3, 3, 1], location=[0, 0, 10])
light_plane.set_name('light_plane')
light_plane_material = bproc.material.create('light_material')


light_point = bproc.types.Light()
light_point.set_energy(200)


light_plane_material.make_emissive(emission_strength=np.random.uniform(1, 6),
                                   emission_color=np.random.uniform([0.5, 0.5, 0.5, 1.0], [1.0, 1.0, 1.0, 1.0]))
light_plane.replace_materials(light_plane_material)
light_point.set_color(np.random.uniform([0.5, 0.5, 0.5], [1, 1, 1]))
location = bproc.sampler.shell(center=[0, 0, 3], radius_min=0.5, radius_max=1,
                               elevation_min=5, elevation_max=89)
light_point.set_location(location)

# ######### set light ########################################################################

area2 = bproc.types.Light()
area2.set_type("AREA")
area2.set_location([0, 0, -3])
area2.set_rotation_euler([math.radians(180), 0, 0])
area2.set_energy(10)
area2.set_color([1, 1, 1])
area2.set_scale([5, 5, 5])

area3 = bproc.types.Light()
area3.set_type("AREA")
area3.set_location([0, 3, 0])
area3.set_rotation_euler([math.radians(-90), 0, 0])
area3.set_energy(10)
area3.set_color([1, 1, 1])
area3.set_scale([5, 5, 5])

area4 = bproc.types.Light()
area4.set_type("AREA")
area4.set_location([0, -3, 0])
area4.set_rotation_euler([math.radians(90), 0, 0])
area4.set_energy(10)
area4.set_color([1, 1, 1])
area4.set_scale([5, 5, 5])

area5 = bproc.types.Light()
area5.set_type("AREA")
area5.set_location([3, 0, 0])
area5.set_rotation_euler([0, math.radians(90), 0])
area5.set_energy(10)
area5.set_color([1, 1, 1])
area5.set_scale([5, 5, 5])

area6 = bproc.types.Light()
area6.set_type("AREA")
area6.set_location([-3, 0, 0])
area6.set_rotation_euler([0, math.radians(-90), 0])
area6.set_energy(10)
area6.set_color([1, 1, 1])
area6.set_scale([5, 5, 5])

# ######### camera ####################################################################################

image_width = 640
image_height = 480
# image_height = 640
bproc.camera.set_resolution(image_width, image_height)


# shuju = np.array([0.43, -0.22, 0.68, 0, 0, 0], dtype=np.double)


shuju = np.array([0, 0, 0.8, 0, 0, 0], dtype=np.double)
camera_position, camera_rotation = shuju[:3], shuju[3: 6]


fx = 609.919868760916
fy = 607.733032143467
cx = 327.571937094492
cy = 241.738191162382
K = np.array([
    [fx, 0, cx],
    [0, fy, cy],
    [0, 0, 1]
])
bproc.camera.set_intrinsics_from_K_matrix(K, image_width, image_height)

cam_poi = [0, 0, 0]  
rotation_matrixrotation_matrix = bproc.camera.rotation_from_forward_vec(cam_poi - camera_position)
cam2world_matrix = bproc.math.build_transformation_mat(camera_position, rotation_matrixrotation_matrix)

bproc.camera.add_camera_pose(cam2world_matrix)
# bpy.data.objects['Camera'].select_set(1)  
bpy.data.cameras['Camera'].angle = 1.23919

# #### world_color ########################################################################################
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.8, 0.749253, 0.749253, 1)


hdr_path = os.path.abspath(os.path.join(os.getcwd(), "hello", "scene_model", "hdr"))

hdr_list = os.listdir(hdr_path)

num_hdr_list = len(hdr_list)

rand_seed = np.random.randint(0, num_hdr_list)
real_hdr_path = os.path.join(hdr_path, hdr_list[rand_seed])

bproc.world.set_world_background_hdr_img(real_hdr_path)


def sample_pose(obj: bproc.types.MeshObject):
    obj.set_location([0, 0, 0])
    obj.set_rotation_euler(bproc.sampler.uniformSO3())  
    obj.set_rotation_euler([0, 0, 0])


def sample_pose_sky(obj: bproc.types.MeshObject):
    # obj.set_location(np.random.uniform([-5, -5, 8], [5, 5, 12]))
    obj.set_location(np.random.uniform([-0.24, -0.2, 0.4], [0.24, 0.2, 1.8]))
    obj.set_rotation_euler(bproc.sampler.uniformSO3())

# bpy.context.object.data.angle = 1.10824

# id = 1
# for obj in bpy.data.objects:
#     if 'lefuqiu' in obj.name:
#         bproc.types.MeshObject(obj).set_cp("category_id", id)
#         id += 1


# sampled_distractor_bop_objs = list(np.random.choice(icbin_dist_bop_objs, size=1, replace=False))
# sampled_distractor_bop_objs += list(np.random.choice(ycbv_dist_bop_objs, size=1, replace=False))
# sampled_distractor_bop_objs += list(np.random.choice(hb_dist_bop_objs, size=1, replace=False))


# for obj in (target_bop_objs + sampled_distractor_bop_objs):
for obj in (target_bop_objs):
    mat = obj.get_materials()[0]
    if obj.get_cp("bop_dataset_name") in ['itodd', 'tless']:
        grey_col = np.random.uniform(0.1, 0.9)
        mat.set_principled_shader_value("Base Color", [grey_col, grey_col, grey_col, 1])
    mat.set_principled_shader_value("Roughness", np.random.uniform(0, 1.0))
    mat.set_principled_shader_value("Specular", np.random.uniform(0, 1.0))
    obj.enable_rigidbody(True, mass=1.0, friction=100.0, linear_damping=0.99, angular_damping=0.99)
    obj.hide(False)



name = target_bop_objs[0].blender_obj.name
for j in range(1, 4):
    for k in range(1, 3):
        bpy.data.objects[name + str(j) + "_" + str(k)].location[2] = 2


for m in range(object_number - 1):
    for j in range(1, 4):
        for k in range(1, 3):
            bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m + 1)].location[2] = 2



mat = bpy.data.materials["Material.008"]
nodes = mat.node_tree.nodes
Material = nodes["Material Output"]
MixShader_node = nodes.new(type="ShaderNodeMixShader")
nodes["Mix Shader"].inputs[0].default_value = 0.5
MixShader_node1 = nodes.new(type="ShaderNodeMixShader")
nodes["Mix Shader.001"].inputs[0].default_value = 0.05
BsdfGlossy_node = nodes.new(type="ShaderNodeBsdfGlossy")
nodes["Glossy BSDF"].inputs[1].default_value = 0.1
BsdfDiffuse_node = nodes.new(type="ShaderNodeBsdfDiffuse")
nodes["Diffuse BSDF"].inputs[1].default_value = 0
nodes["Diffuse BSDF"].inputs[0].default_value = (0, 0.302509, 0.8, 1)

BsdfGlossy_node1 = nodes.new(type="ShaderNodeBsdfGlossy")
nodes["Glossy BSDF.001"].inputs[1].default_value = 0

links = mat.node_tree.links
links.new(MixShader_node.outputs[0], Material.inputs[0])
links.new(MixShader_node1.outputs[0], MixShader_node.inputs[1])
links.new(BsdfGlossy_node.outputs[0], MixShader_node.inputs[2])
links.new(BsdfDiffuse_node.outputs[0], MixShader_node1.inputs[1])
links.new(BsdfGlossy_node1.outputs[0], MixShader_node1.inputs[2])


bproc.object.sample_poses(
    # objects_to_sample=target_bop_objs + sampled_distractor_bop_objs, 
    objects_to_sample=target_bop_objs,  
    sample_pose_func=sample_pose_sky,  
    # objects_to_check_collisions=sampled_target_bop_objs,
)


LBox.enable_rigidbody(active=False, collision_shape="MESH", friction=1, mass=1)


for obj in target_bop_objs:
    obj.enable_rigidbody(active=True, collision_shape="BOX", friction=1, mass=1)


bproc.object.simulate_physics_and_fix_final_poses(min_simulation_time=4,
                                                  max_simulation_time=20,
                                                  check_object_interval=1)


# bop_bvh_tree = bproc.object.create_bvh_tree_multi_objects(target_bop_objs + sampled_distractor_bop_objs)
bop_bvh_tree = bproc.object.create_bvh_tree_multi_objects(target_bop_objs)

cam_poses = 0
while cam_poses < 5:

    location = bproc.sampler.shell(center=[0, 0, 0],
                                   radius_min=0.45,
                                   radius_max=1.08,
                                   elevation_min=50,
                                   elevation_max=90)

    poi = bproc.object.compute_poi(np.random.choice(target_bop_objs, size=object_number, replace=False))

    # rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location,
    #                                                          inplane_rot=np.random.uniform(-3.14159, 3.14159))
    rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location)
 
    cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)


    if bproc.camera.perform_obstacle_in_view_check(cam2world_matrix, {"min": 0.3}, bop_bvh_tree):

        bproc.camera.add_camera_pose(cam2world_matrix, frame=cam_poses)
        cam_poses += 1


# id = 100
# for obj in bpy.data.objects:
#     if 'Cube' or 'wooden_table_02' in obj.name:
#         bproc.types.MeshObject(obj).set_cp("category_id", id)
#         id += 1
#
# bpy.data.objects["Cube"].hide_render = True



# bproc.renderer.enable_normals_output()
bproc.renderer.enable_depth_output(activate_antialiasing=False)
# bproc.renderer.enable_diffuse_color_output()

data0 = bproc.renderer.render()


bproc.writer.write_bop(os.path.join(args.output_dir, 'test_bop_data'),
                       target_objects=target_bop_objs,
                       dataset='ourssix', 
                       depth_scale=0.05,
                       depths=data0["depth"],
                       colors=data0["colors"],
                       color_file_format="PNG",
                       append_to_existing_output=True)


for i in range(3):
    for j in range(1, 4):
        for k in range(1, 3):
            bpy.data.objects[name + str(j) + "_" + str(k)].location[i] = bpy.data.objects[name].location[i]
            bpy.data.objects[name + str(j) + "_" + str(k)].rotation_euler[i] = \
            bpy.data.objects[name].rotation_euler[i]


for m in range(object_number - 1):
    for i in range(3):
        for j in range(1, 4):
            for k in range(1, 3):
                bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m + 1)].location[i] = \
                bpy.data.objects[name + ".00" + str(m + 1)].location[i]
                bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m + 1)].rotation_euler[i] = \
                bpy.data.objects[name + ".00" + str(m + 1)].rotation_euler[i]

# for i in range(object_number):
#     bpy.context.scene.collection.objects.unlink(target_bop_objs[i].blender_obj)

for obj in (target_bop_objs):
    obj.disable_rigidbody()
    obj.hide(True)


camera = bpy.context.scene.camera

euler = camera.matrix_world.to_euler('XYZ')
mat1 = Matrix.Rotation(euler.x, 4, 'X')
mat2 = Matrix.Rotation(euler.y, 4, 'Y')
mat3 = Matrix.Rotation(euler.z, 4, 'Z')
mat = mat1 @ mat2 @ mat3

v1 = mat @ Vector((0, 0, -1))

# ### six face ############################################################################################
obj = []
obj1 = []
obj2 = []
obj3 = []
obj4 = []
obj5 = []
obj6 = []
obj7 = []


for m in range(1, object_number+1):
    for j in range(1, 4):
        for k in range(1, 3):
            if m == 1:
                obj.append(bpy.data.objects[name + str(j) + "_" + str(k)])
            elif m == 2:
                obj1.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 3:
                obj2.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 4:
                obj3.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 5:
                obj4.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 6:
                obj5.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 7:
                obj6.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])
            elif m == 8:
                obj7.append(bpy.data.objects[name + str(j) + "_" + str(k) + ".00" + str(m - 1)])


k = 1
max1 = 60   
max2 = 45   
max3 = 30   

OBJ = []
for m in range(1, object_number+1):
    if m == 1:
        OBJ = obj
        NAME = name + '1_1'
        NAME1 = name + '1_2'
        NAME2 = name + '2_1'
        NAME3 = name + '2_2'
        NAME4 = name + '3_1'
        NAME5 = name + '3_2'

    elif m == 2:
        OBJ = obj1
        NAME = name + '1_1.001'
        NAME1 = name + '1_2.001'
        NAME2 = name + '2_1.001'
        NAME3 = name + '2_2.001'
        NAME4 = name + '3_1.001'
        NAME5 = name + '3_2.001'

    elif m == 3:
        OBJ = obj2
        NAME = name + '1_1.002'
        NAME1 = name + '1_2.002'
        NAME2 = name + '2_1.002'
        NAME3 = name + '2_2.002'
        NAME4 = name + '3_1.002'
        NAME5 = name + '3_2.002'

    elif m == 4:
        OBJ = obj3
        NAME = name + '1_1.003'
        NAME1 = name + '1_2.003'
        NAME2 = name + '2_1.003'
        NAME3 = name + '2_2.003'
        NAME4 = name + '3_1.003'
        NAME5 = name + '3_2.003'

    elif m == 5:
        OBJ = obj4
        NAME = name + '1_1.004'
        NAME1 = name + '1_2.004'
        NAME2 = name + '2_1.004'
        NAME3 = name + '2_2.004'
        NAME4 = name + '3_1.004'
        NAME5 = name + '3_2.004'

    elif m == 6:
        OBJ = obj5
        NAME = name + '1_1.005'
        NAME1 = name + '1_2.005'
        NAME2 = name + '2_1.005'
        NAME3 = name + '2_2.005'
        NAME4 = name + '3_1.005'
        NAME5 = name + '3_2.005'

    elif m == 7:
        OBJ = obj6
        NAME = name + '1_1.006'
        NAME1 = name + '1_2.006'
        NAME2 = name + '2_1.006'
        NAME3 = name + '2_2.006'
        NAME4 = name + '3_1.006'
        NAME5 = name + '3_2.006'

    elif m == 8:
        OBJ = obj7
        NAME = name + '1_1.007'
        NAME1 = name + '1_2.007'
        NAME2 = name + '2_1.007'
        NAME3 = name + '2_2.007'
        NAME4 = name + '3_1.007'
        NAME5 = name + '3_2.007'


    for j in range(6):
        bproc.types.MeshObject(OBJ[j]).set_cp("category_id", k)
        k = k + 1

        if j == 0:
            ob = bpy.data.objects[NAME]
        elif j == 1:
            ob = bpy.data.objects[NAME1]
        elif j == 2:
            ob = bpy.data.objects[NAME2]
        elif j == 3:
            ob = bpy.data.objects[NAME3]
        elif j == 4:
            ob = bpy.data.objects[NAME4]
        elif j == 5:
            ob = bpy.data.objects[NAME5]

        bpy.context.view_layer.update()

        euler = ob.matrix_world.to_euler('XYZ')
        mat1 = Matrix.Rotation(euler.z, 4, 'Z')
        mat2 = Matrix.Rotation(euler.y, 4, 'Y')
        mat3 = Matrix.Rotation(euler.x, 4, 'X')
        mat = mat1 @ mat2 @ mat3
        norm = mat @ ob.data.polygons[0].normal

        radian = acos(v1 @ norm)
        angle = 180 - math.degrees(radian)
        # print(angle)

        if (j == 0 or j == 1) and (angle > max1):
            bproc.types.MeshObject(OBJ[j]).set_cp("category_id", 0)
        elif (j == 2 or j == 3) and (angle > max2):
            bproc.types.MeshObject(OBJ[j]).set_cp("category_id", 0)
        elif (j == 4 or j == 5) and (angle > max3):
            bproc.types.MeshObject(OBJ[j]).set_cp("category_id", 0)



seg_data = bproc.renderer.render_segmap(map_by=["instance", "class", "name"])
# print(seg_data['instance_attribute_maps'][0])



bproc.renderer.enable_normals_output()

data = bproc.renderer.render()


bproc.writer.write_coco_annotations(os.path.join(args.output_dir, 'test_coco_data'),
                        instance_segmaps=seg_data["instance_segmaps"],
                        instance_attribute_maps=seg_data["instance_attribute_maps"],
                        colors=data["colors"],
                        color_file_format="PNG",
                        mask_encoding_format='polygon',
                        append_to_existing_output=True)

# write the data to a .hdf5 container
# bproc.writer.write_hdf5(os.path.join(args.output_dir, 'test_hdf5_data'), data)

print("end_success")



