#!/usr/bin/python
import xml.dom.minidom
import sys
import time
import json

if __name__ == '__main__':

	try:
		svgFile = open(sys.argv[1], 'rb')
		jsFile = open(sys.argv[2], 'wb')
		jsonObjectName = sys.argv[2].split('.')[0]

		print 'Extracting all path elements...'
		dom = xml.dom.minidom.parse(svgFile)
		svgFile.close()
		paths = {}
	
		for pathTag in dom.getElementsByTagName('path'):
			paths[pathTag.getAttribute('id')] = pathTag.getAttribute('d')
		print 'Processed ' + str(len(paths)) + ' paths in ' + sys.argv[1]
	
		jsFile.write('var ' + jsonObjectName + ' = ' + json.dumps(paths, sort_keys=True, indent=4) + ';')
		jsFile.close()
	except:
		#pass
		print sys.exc_info()
		print 'usage: %(cmd)s <input svg file> <output js file>' % {'cmd' : sys.argv[0] }
