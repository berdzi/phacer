Quick and dirty script to organize photos into three folders -> selfies , group photos and without faces. Helps me when my friends wants me to share my photos with them and I don't want to share selfies, only group pictures.
It detects faces and counts them 

1-2 - selfie
&lt;2 - group photos
0 - no faces

create folders nofaces,selfies,group at the same level as the photos folder

Requires python, opencv and numpy

Usage: python phacer.py folder_with_photos
