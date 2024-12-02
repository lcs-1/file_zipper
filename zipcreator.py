import zipfile
import pathlib

def myzip(filepaths, dest_dir):
    destpath = pathlib.Path(dest_dir, "compressed.zip")  # Create the destination path
    with zipfile.ZipFile(destpath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)  # Write each file into the archive
