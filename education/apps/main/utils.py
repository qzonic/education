import os


def get_material_upload_path(instance, filename):
    return os.path.join(
      '%s' % instance.slug, filename
    )


def get_slide_upload_path(instance, filename):
    return os.path.join(
      '%s' % instance.material.slug, 'slides', filename
    )
