def clean_file_directory():
  static_folder = os.listdir(os.path.join(settings.STATIC_ROOT, 'files'))
  for files in static_folder:
    os.remove(os.path.join(os.path.join(settings.STATIC_ROOT, 'files'), files))