import bpy

class MOD_OT_ImportReferenceImage(bpy.types.Operator):
    bl_idname = 'mod.import_reference_image'
    bl_label = 'Import Reference Image'
    
    def execute(self, context):

        return { 'FINISHED' }
    
    def invoke(self, context, event):
        return self.execute(context)


classes = [
    MOD_OT_ImportReferenceImage,
]

def register():
    ## Props
    bpy.types.Scene.mod_reference_image = bpy.props.StringProperty(name="mode_reference_image", default="", subtype="FILE_PATH")
    

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
    del bpy.types.Scene.mod_reference_image
