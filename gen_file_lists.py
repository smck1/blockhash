import os
import random
from sys import argv


path = ''
outpath="./"
if len(argv) == 2:
    path = argv[1]
elif len(argv) ==3:
    path = argv[1]
    outpath = argv[2]
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


print "Saving {} file paths to {}".format(len(flist), outpath)


f = open(outpath, "w")
for x in flist:
    f.write("{}\n".format(x))
f.close()
exit()
