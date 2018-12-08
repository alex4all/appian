import fnmatch
import os

print("Script started")
for root, dirnames, filenames in os.walk('.'):
	if "./." in root or "installers" in root:
		continue
	for filename in fnmatch.filter(filenames, '*'):
		if filename.startswith( '.' ):
			continue
		print(os.path.join(root, filename))
print("Script complete")
