from ObjProcessing import Obj

vertices, faces = Obj.ReadObj('average_boy_6-8.obj')
new_obj = Obj.newObj(vertices, faces)
print(new_obj)
