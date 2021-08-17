
import os
import zipfile
import shutil


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))


def create_zip():
    zipf = zipfile.ZipFile('final.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./downloads/', zipf)
    zipf.close()
    shutil.rmtree('downloads')