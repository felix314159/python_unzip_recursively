import os
import io
import zipfile


def unzip_all():
    for filename in os.listdir("."):
        if filename.endswith(".zip"):
            z = zipfile.ZipFile(filename)
            for f in z.namelist():
                dirname = os.path.splitext(f)[0]  
                os.mkdir(dirname)
                content = io.BytesIO(z.read(f))
                zip_file = zipfile.ZipFile(content)
                for i in zip_file.namelist():
                    zip_file.extract(i, dirname)
                    

unzip_all()