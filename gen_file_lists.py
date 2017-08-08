import os
import random
from sys import argv


path = ''
output_dir="./"
if len(argv) == 2:
    path = argv[1]
elif len(argv) ==3:
    path = argv[1]
    output_dir = argv[2]
else:
    print "Usage: <path_to_dir> optional:<outputfile>"
    exit()

print "Walking directory: {}".format(path)

flist = []
for subdir, dirs, files in os.walk(path):
    for f in files:
        fpath = os.path.abspath(os.path.join(subdir, f))
        fname, ext = os.path.splitext(fpath)
        ext = ext.lower()
        if ext in [".jpeg",".jpg", ".png", ".gif"]:
            flist.append(fpath)

outpath = os.path.join(output_dir,"filelist.txt")
print "Saving {} file paths to {}".format(len(flist), outpath)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

f = open(os.path.join(outpath), "w")
for x in flist:
    f.write("{}\n".format(x))
f.close()
exit()
