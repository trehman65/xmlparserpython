from __future__ import division
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
import cv2

outputLines=[]
finalOutputJson=sys.argv[2]
xmldoc = minidom.parse(sys.argv[1])
# img = cv2.imread('/Users/talha/Documents/currentworkspace/xmlomni/xml2jsonLineLevel/1.jpeg')
# finalOutputImage="/Users/talha/Documents/currentworkspace/xmlomni/xml2jsonLineLevel/1-seg.jpeg"

lines = xmldoc.getElementsByTagName('ln')
lenLines = len(lines)
factor=300/1440

count=1;

for s in lines:

	if count > lenLines:
		break

	words = s.getElementsByTagName('wd')
	thisLine=""

	for t in words:
		thisWord=t.childNodes[0].nodeValue
		if(thisWord!=None):
			thisLine = thisLine + thisWord + " "

	l=float(s.attributes['l'].value)*factor
	r=float(s.attributes['r'].value)*factor
	t=float(s.attributes['t'].value)*factor
	b=float(s.attributes['b'].value)*factor
	
	#cv2.rectangle(img,l, t, r, b, (0, 0, 255), 3)
	
	#cv2.rectangle(img,(int(l), int(t)), (int(r), int(b)), (0, 0, 255), 3)
	#cv2.rectangle(img,(154,1147), (1546,1277), (0, 0, 255), 3)
	
	temp={}
	temp["id"]=count
	temp["l"]=l
	temp["r"]=r
	temp["t"]=t
	temp["b"]=b
	temp["text"]=thisLine

	outputLines.append(temp)
	print thisLine
	count=count+1

cv2.imwrite(finalOutputImage,img)


with open(finalOutputJson, 'w') as outfile:  
        json.dump(outputLines, outfile)