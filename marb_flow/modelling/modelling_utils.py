import bpy
import mathutils
import os

from ..utils.logging_helper import log_console_message


def create_collection(collection_name: str, parent_collection: str = None) -> bpy.types.Collection:
    if collection_name in bpy.data.collections:
        log_console_message('WARNING', f'Collection {collection_name} already exists')
        return bpy.data.collections[collection_name]
    
    collection = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(collection)
    if parent_collection:
        parent_collection.children.link(collection)

    return collection
    
def create_ref_plane(ref_img: bpy.types.Image, ref_plane_name: str, ref_plane_loc: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)), ref_plane_rot: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),) -> bpy.types.Object:
    bpy.ops.object.empty_add(type='IMAGE', align='WORLD', location=ref_plane_loc, rotation=ref_plane_rot, scale=(1.0, 1.0, 1.0))
    ref_plane = bpy.context.object
    ref_plane.name = ref_plane_name
    # ref_plane.data.name = f"{ref_plane_name}_mesh" # Doesn't make any fucking sense because it has NO mesh (being an empty....)
    ref_plane.data = ref_img
    
    return ref_plane

def unlink_from_collections(obj: bpy.types.Object) -> None:
    for collection in obj.users_collection:
        collection.objects.unlink(obj)


def check_import_image_path(import_path: str) -> str:
    """ Returns input path if path is valid

    Checks if the path is valid, exists and can be read.
    Raises errors if there's a problem with the path.

    Args:
        import_path: The path to check

    Returns:
        The input path.

    Raises:
        FileExistsError : If file does not exist
    """
    if not os.path.exists(import_path):
        raise FileExistsError(f'{import_path} does not exist')
    if not import_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.tif')):
        raise ValueError(f'{import_path} is not a valid image file')

    return import_path