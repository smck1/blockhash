blockhash
=========

This is a perceptual image hash calculation tool based on algorithm descibed in
Block Mean Value Based Image Perceptual Hashing by Bian Yang, Fan Gu and Xiamu Niu.

Fork
-----
The purpose of the fork is to allow for a large number of files to be hashed in parallel.


Build and install
-----------------

Blockhash requires libmagickwand. On Debian/Ubuntu it can be installed using
the following command:

    sudo apt-get install libmagickwand-dev

On Fedora and friends:

    sudo dnf install ImageMagick-devel
	
Requires libboost thread, system and filesystem. 
TODO: Make waf handle this.

To build blockhash cd to the source directory and type:

    ./waf configure
    ./waf

The program binary will land in `./build`. To install it to `/usr/local/bin/` type:

    ./waf install


Usage
-----

Run `blockhash pathto_filelist.txt` for calculating hashes.

Run `blockhash --help` for the list of options.

License
-------

Copyright 2014 Commons Machinery http://commonsmachinery.se/

Distributed under an MIT license, please see LICENSE in the top dir.

Contact: dev@commonsmachinery.se
