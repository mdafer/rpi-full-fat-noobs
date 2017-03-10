#!/usr/bin/python
'''
Raspberry Pi Full Fat Noobs
by Mostafa Dafer
Part of the download function by PabloG
v0.1
'''

import requests, urllib2, os#,sys

oses = requests.get('https://downloads.raspberrypi.org/os_list_v3.json')
myList=[1,5,8,11,13]

def download(url, file_name= None, directory=None):
	if not file_name:
		file_name = url.split('/')[-1]
	if directory:
		if not os.path.exists(directory):
			os.makedirs(directory)
		file_name = directory+"/"+file_name
	existSize = 0
	if os.path.exists(file_name):
		f = open(file_name, 'ab')
		existSize = os.path.getsize(file_name)
	else:
		f = open(file_name, 'wb')

	completereq = urllib2.Request(url, headers={'User-Agent' : "Raspberry Pi Full Fat Noobs"}) 
	completeu = urllib2.urlopen(completereq)
	completeFileSize = int(completeu.info().getheaders("Content-Length")[0])

	if completeFileSize == existSize:
		print 'already downloaded: '+file_name
		#sys.exit(0)
		f.close()
		return
		
	req = urllib2.Request(url, headers={'User-Agent' : "Raspberry Pi Full Fat Noobs",'Range': 'bytes=%d-' % (existSize, )}) 
	u = urllib2.urlopen(req)
	
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	
	if file_size+existSize!=completeFileSize:
		print 'error resuming, redownloading now'
		f = open(file_name, 'wb')
		file_size = completeFileSize
		existSize = 0
		
	print "Downloading: %s Bytes To Download: %s Total: %s" % (file_name, file_size, completeFileSize)

	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break
		existSize += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (existSize, existSize * 100. / completeFileSize)
		status = status + chr(8)*(len(status)+1)
		print status
	f.close()
	return 
	
print "Raspberry Pi Full Fat Noobs here!";

#print json.dumps(oses.json(), indent=4, separators=(',', ': '))

osList = enumerate(oses.json()["os_list"])
print "\nAvailable OS:"
for (i, myos) in osList:
	print i, myos['os_name']
	
osList = enumerate(oses.json()["os_list"])
print "\n\nChosen OS:"
for (i, myos) in osList:
	if i in myList:
		print i, myos['os_name']
		
osList = enumerate(oses.json()["os_list"])
print "\n\nChosen OS:"
for (i, myos) in osList:
	if i in myList:
		print i, myos['os_name']
		if myos['icon']:
			download(myos['icon'],None,myos['os_name'])
		if myos['partition_setup']:
			download(myos['partition_setup'],None,myos['os_name'])
		if myos['partitions_info']:
			download(myos['partitions_info'],None,myos['os_name'])
		if myos['os_info']:
			download(myos['os_info'],None,myos['os_name'])
		for (tarball) in myos['tarballs']:
			if tarball:
				download(tarball,None,myos['os_name'])
		