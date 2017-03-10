# rpi-full-fat-noobs
With RPi Full Fat Noobs you can add any Raspberry Pi Noobs OS to the offline installer

This is a simple python 2.7 script that downloads all necessary files of selected additional OS to Noobs for offline installation.

The link to the OS json file is hardcoded on line 11 ('https://downloads.raspberrypi.org/os_list_v3.json')

The list of chosen OS to download is hardcoded on line 12 (myList=[1,5,8,11,13])
each number represents the index of the selected OS, to check all OS before selecting any, replace line 12 with: myList=[]

The downloader also enables auto-resume by default and can detect whether server supports resume or not automatically.

![alt tag](https://github.com/mdafer/rpi-full-fat-noobs/blob/master/in_action.jpg)