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

tags=sys.argv[1].split('/')
filename=tags[len(tags)-1].replace('.xml',"")
directory=sys.argv[1].replace(tags[len(tags)-1],"")
finalOutputJson=directory+filename+'.json'



# img = cv2.imread('/Users/talha/Documents/currentworkspace/xmlomni/xml2jsonLineLevel/2.jpeg')
# finalOutputImage="/Users/talha/Documents/currentworkspace/xmlomni/xml2jsonLineLevel/2-seg.jpeg"

xmldoc = minidom.parse(sys.argv[1])
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

	l=int(float(s.attributes['l'].value)*factor)
	r=int(float(s.attributes['r'].value)*factor)
	t=int(float(s.attributes['t'].value)*factor)
	b=int(float(s.attributes['b'].value)*factor)

	
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

# cv2.imwrite(finalOutputImage,img)


with open(finalOutputJson, 'w') as outfile:  
        json.dump(outputLines, outfile)