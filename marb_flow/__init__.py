import bpy

bl_info = {
    'name' : 'Martin Blender Workflow',
    'blender' : (4, 1, 0),
    'version' : (0, 1, 0),
}

class MBW_PT_MainPanel(bpy.types.Panel):
    bl_idname = "MBW_PT_main"
    bl_label = "Martin Blender Workflow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MBW"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Martin's Blender tools and stuff")

classes = [
    MBW_PT_MainPanel,
]

def register():
    ## Props

    ## Operators

    ## UI
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    ## UI
    for cls in classes.reverse:
        bpy.utils.unregister_class(cls)
    ## Operators

    ## Props
    pass

if __name__ == "__main__":
    register()