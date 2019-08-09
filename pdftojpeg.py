import os
import tempfile
import shutil
from pdf2image import convert_from_path
 
try:
    result_folder = "./first_page_images"
    os.mkdir("./first_page_images")
except OSError:
    print ("Creation of the directory %s failed" % result_folder)
else:
    print ("Successfully created the directory %s " % result_folder)

files = []
for r, d, f in os.walk("./"):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

with tempfile.TemporaryDirectory() as path:
    for file in files:
        pages = convert_from_path(file, dpi=300, output_folder=path, fmt='png', last_page=1, first_page=0, thread_count=1)
        pages[0].close()
        file2 = os.listdir(path)[0]
        jpgfile = os.path.join(path, file2)
        shutil.move(jpgfile, f'./first_page_images/{os.path.splitext(os.path.basename(file))[0]}.png')