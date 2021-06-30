
    
    
    
    
bl_info = {
    "name": "Focus on first selection island",
    "category": "Mesh",
    "blender": (2, 80, 0)
}

import bpy
import bmesh
import random


class FocusOnFirstSelectionIsland(bpy.types.Operator):
    """Focus on first selection island""" 
    bl_idname = "object.focus_on_first_selection_island"        # unique identifier for buttons and menu items to reference.
    bl_label = "Focus island"         						  # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  	
    
    def execute(self, context):        # execute() is called by blender when running the operator.

        obj = bpy.context.edit_object
        mesh = obj.data
        bmes = bmesh.from_edit_mesh(mesh)

        found = False

        for face in bmes.faces:
            if not found and face.select:
                found = True
            elif face.select:
                face.select = False

        if found:
            bpy.ops.view3d.view_selected()

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(FocusOnFirstSelectionIsland.bl_idname)		
        
def register():
    bpy.utils.register_class(FocusOnFirstSelectionIsland)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)

def unregister():
    bpy.utils.unregister_class(FocusOnFirstSelectionIsland)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
