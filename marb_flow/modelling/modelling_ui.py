import bpy

from . import modelling_operator

class MOD_PT_MainPanel(bpy.types.Panel):
    bl_idname = 'MOD_PT_main'
    bl_label = 'Modelling'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MBW'
    bl_parent_id = 'MBW_PT_main'
    
    def draw(self, context):
        layout = self.layout
        row_ref_img = layout.row()
        row_ref_img.prop(context.scene, 'mod_reference_image', text='Reference Image')
        row_ref_img.operator(modelling_operator.MOD_OT_ImportReferenceImage.bl_idname, text=modelling_operator.MOD_OT_ImportReferenceImage.bl_label)
        
        # return super().draw(context)


classes = [
    MOD_PT_MainPanel,
]

def register():
    ## Props

    ## Operators
    
    ## Classes
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    ## Classes
    for cls in classes.reverse:
        bpy.utils.unregister_class(cls)

    ## Operators

    ## Props