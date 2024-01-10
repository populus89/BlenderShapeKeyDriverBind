import bpy
from mathutils import *


#Binds the shapekeys of the target mesh to the source mesh with drivers


#Use MESH names not OBJECT names!

srcObject = "src mesh name"

trgObject = "target mesh name"

srcData = bpy.data.objects[srcObject].data.shape_keys.key_blocks

trgData = bpy.data.objects[trgObject].data.shape_keys.key_blocks


for k in srcData:
        shape = trgData.find(k.name)
        if shape is not None:
            sk1 = k
            sk1_datapath = k.path_from_id("value")
            fcurve = trgData[shape].driver_add("value")
            var = fcurve.driver.variables.new()
            fcurve.driver.type = "AVERAGE"
            target = var.targets[0]
            target.id_type = "KEY"
            target.id = bpy.data.shape_keys[bpy.data.objects[srcObject].active_shape_key.id_data.name]
            target.data_path = sk1_datapath
            
            fcurve.keyframe_points.insert(0,0)
            fcurve.keyframe_points.insert(1,1)
