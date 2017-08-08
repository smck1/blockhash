#!/bin/sh
python ./gen_file_lists.py testdata/
build/blockhash -b 16 -f filelist.txt
