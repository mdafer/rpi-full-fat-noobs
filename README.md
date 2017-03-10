# rpi-full-fat-noobs
Add any Raspberry Pi Noobs OS to the offline installer

This is a simple python 2.7 script that downloads all necessary files of selected additional OS to Noobs for offline installation.

The link to the OS json file is hardcoded on line 11 ('https://downloads.raspberrypi.org/os_list_v3.json')

The list of chosen OS to download is hardcoded on line 12 (myList=[1,5,8,11,13])
each number represents the index of the selected OS, to check all OS before selecting any, replace line 12 with: myList=[]