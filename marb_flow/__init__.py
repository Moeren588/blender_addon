import bpy

from .utils.logging_helper import log_console_message

from .modelling import modelling_ui, modelling_operator

bl_info = {
    'name' : 'Martin Blender Workflow',
    'author' : 'Martin Moen',
    'description' : 'My own Blender tools with tools I find useful',
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
        layout.label(text=f"MB Flow {bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}")

classes = [
    MBW_PT_MainPanel,
]

def register():
    # Main
    for cls in classes:
        bpy.utils.register_class(cls)

    # Modelling
    modelling_operator.register()
    modelling_ui.register()

    log_console_message('sys', f'Loaded Martin Blender Workflow v.{bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}')

def unregister():
    # Modelling
    modelling_ui.unregister()
    modelling_operator.unregister()
    
    # Main
    for cls in classes.reverse:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()