#! /usr/bin/python
# coding = utf-8

import os, time, sys

formats = ["jpg", "gif", "png"]			# approved extensions
media_path = "../media/"			# relative path to media folder
overlay_file = "../media/overlay.png"		# filename of the overlay
files = os.listdir(media_path)			# read filenames into a list
delay = 10					# seconds of delay between slides

# remove any files that don't end with an approved extension

###  files = [n for n in files if n not in filter(lambda a: not(a[-3:] in formats), files)]
files = [n for n in sorted(files) if n.endswith(tuple(formats))]

#  remove the overlay from the rotation, raise an error if there isn't one
try:
    files.remove(overlay_file)
except ValueError:
    print("No Overlay detected")

x = -1
stored_exception = None

print "there are %s valid files" % len(files)

try:
	while True:
		if x == len(files)-1: 
			x = 0
		else:
			x = x+1

		print "index %s is %s " % (x, files[x])

		body = '''
<html>
	<head>
		<meta http-equiv="refresh" content="''' + str(delay) + '''">
	</head>
	<body>
		<img src="''' + files[x] + '''" style="position: fixed; top:0; left:0; right: 0; bottom: 0; width: 100%; height: 100%; z-index: 1;">
		<img src="''' + overlay_file + '''" style="position: fixed; top:0; left:0; right: 0; bottom: 0; width: 100%; height: 100%; z-index: 99;">
	</body>
</html>'''

		with open("../output.html", "w") as f:
			f.write(body)

		time.sleep(delay)
        
except KeyboardInterrupt:
    stored_exception=sys.exc_info()

if stored_exception:
	print ("\n\nexiting \n")
	sys.exit()
