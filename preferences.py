import bpy
import importlib

class IGcodePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        flag = importlib.util.find_spec('regex') is not None and importlib.util.find_spec('tqdm') is not None
        if flag:
            layout.label(text='Regex and Tqdm loaded.', icon='INFO')
        else:
            layout.label(text='import-G-code requires Regex and Tqdm!', icon='ERROR')
            row = layout.row()
            row.operator('igcode.installer', text='Install Regex and Tqdm')

class IGcodeInstaller(bpy.types.Operator):
    bl_idname = "igcode.installer"
    bl_label = "Install Regex and Tqdm"
    bl_description = "Install Regex and Tqdm"

    def execute(self, context):
        try:
            from .utils_pip import Pip
            Pip.install('regex')
            Pip.install('tqdm')
            self.report({'INFO'}, 'Successfully installed Regex and Tqdm.')
        except Exception as e:
            self.report({'ERROR'}, f'Could not install Regex and Tqdm: {e}')
        return {'FINISHED'}

def register():
    bpy.utils.register_class(IGcodePreferences)
    bpy.utils.register_class(IGcodeInstaller)

def unregister():
    bpy.utils.unregister_class(IGcodePreferences)
    bpy.utils.unregister_class(IGcodeInstaller)