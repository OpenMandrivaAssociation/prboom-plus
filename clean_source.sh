#!/bin/sh -ex
# Remove Wolfenstein dogs from source

: ${DOOMWADDIR:=/usr/share/doom};

version=$(perl -lne 'if(/^Version\s*:\s*(\S+)/){print$1;exit}' <prboom-plus.spec);
tar -xf "prboom-plus-$version.tar.xz";
pushd "prboom-plus-$version/data/";
deutex -doom2 "$DOOMWADDIR" -extract prboom-plus.wad;
touch lumps/{b,c}_{start,end}.lmp;
grep -Ev '^DOG|^DSDG' <prboom.txt >wadinfo.txt;
rm -f prboom-plus.wad;
deutex -doom2 "$DOOMWADDIR" -create wadinfo.txt prboom-plus.wad;
find . -mindepth 1 -type d -print0 | xargs -0 rm -Rf;
mv wadinfo.txt prboom.txt;
rm -f error.txt output.txt;
popd;
find "prboom-plus-$version" -print0 | sort -z | \
	tar -T- --null --use=xz -cvf "prboom-plus-$version+.tar.xz";
