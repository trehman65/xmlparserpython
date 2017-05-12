from xml.dom import minidom
import io
import os
import glob
import csv
import cv2
import sys
import re
import natsort
import time
import sys
import json
import os.path

lines={}
finalOutputJson="/Users/talha/Desktop/xmlomni/output.json"
xmldoc = minidom.parse('/Users/talha/Desktop/1.xml')

lines = xmldoc.getElementsByTagName('ln')
print len(lines)
print lines

count=1;
for s in lines:
	words = s.getElementsByTagName('wd')
	thisLine=""

	for t in words:
		thisLine = thisLine + t.childNodes[0].nodeValue+ " "
	
	l=s.attributes['l'].value
	r=s.attributes['r'].value
	t=s.attributes['t'].value
	b=s.attributes['b'].value
	
	temp={}
	temp["id"]=count
	temp["l"]=l
	temp["r"]=r
	temp["t"]=t
	temp["b"]=b
	temp["text"]=thisLine

	lines.append(temp)
	print thisLine
	cout=count+1

with open(finalOutputJson, 'w') as outfile:  
        json.dump(lines, outfile)