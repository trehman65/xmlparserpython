
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

words=[]
finalOutputJson="/Users/talha/Desktop/xmlomni/output.json"
xmldoc = minidom.parse('/Users/talha/Desktop/1.xml')

itemlist = xmldoc.getElementsByTagName('wd')
print(len(itemlist))

for s in itemlist:
	words.append(s.childNodes[0].nodeValue)
	print(s.childNodes[0].nodeValue)

with open(finalOutputJson, 'w') as outfile:  
        json.dump(words, outfile)