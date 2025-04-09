import bpy
import mathutils
import math

from . import modelling_utils
from ..utils.logging_helper import log_console_message


class MOD_OT_ImportReferenceImage(bpy.types.Operator):
    bl_idname = 'mod.import_reference_image'
    bl_label = 'Import Reference Image'

    ref_img : bpy.types.Image
    
    def execute(self, context):
        log_console_message('debug', f'Testing reference image importer and setup. Found {self.ref_img.name_full}')
        ref_collection = modelling_utils.create_collection('_references')
        top_ref = modelling_utils.create_ref_plane(self.ref_img, 'top_ref')
        modelling_utils.unlink_from_collections(top_ref)
        ref_collection.objects.link(top_ref)

        side_ref = modelling_utils.create_ref_plane(self.ref_img, 'side_ref', ref_plane_rot=mathutils.Vector((math.pi, 0.0, math.pi)))
        modelling_utils.unlink_from_collections(side_ref)
        ref_collection.objects.link(side_ref)

        log_console_message('finish', f'Finished adding reference images of {self.ref_img.name}')
        return { 'FINISHED' }
    
    def invoke(self, context, event):
        # Check filepath
        try:
            modelling_utils.check_import_image_path(context.scene.mod_reference_image)
        except FileExistsError:
            log_console_message('error', f'{context.scene.mod_reference_image} does not exist')
            self.report({'ERROR'}, f'{context.scene.mod_reference_image} does not exist')
            return {'CANCELLED'}
        except ValueError:
            log_console_message('error', f'{context.scene.mod_reference_image} is not a valid image file')
            self.report({'ERROR'}, f'{context.scene.mod_reference_image} is not a valid image file')
            return {'CANCELLED'}
        
        try:
            self.ref_img = bpy.data.images.load(context.scene.mod_reference_image)
        except RuntimeError as e:
            log_console_message('error', f'Error loading reference image: {e}')
            self.report({'ERROR'}, f'Error loading reference image: {e}')
            return {'CANCELLED'}

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
