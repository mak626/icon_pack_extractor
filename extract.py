# importing required modules
from ast import Num
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import re
import shutil
import os
import sys

try:
    file_name = sys.argv[1]
except:
    print('No file name given..')
    exit(0)
extractPath = 'temp'
appFilterPath = 'temp/assets/appfilter.xml'
iconPath = 'temp/res/drawable-nodpi-v4'
destinationPath = 'icons'

print("Removing pre-existing directories if any..")
try:
    shutil.rmtree(path=destinationPath)
except:
    pass

with ZipFile(file_name, 'r') as zip:
    print('Extracting the apk now...')
    zip.extractall(extractPath)
    print('Done!')


tree = ET.parse(appFilterPath)
root = tree.getroot()
try:
    os.mkdir(destinationPath)
except:
    pass


print('Extracting all the icons now...')
for item in root.findall('item'):
    drawableName = item.get('drawable') + '.png'
    pkgName = ""
    m = re.search('{(.*)\/', item.get('component'))
    if m:
        pkgName = m.group(1) + '.png'

    if(pkgName != ""):
        srcIconPath = iconPath + '/' + drawableName
        destPkgPath = destinationPath + '/' + pkgName
        try:
            os.rename(srcIconPath, destPkgPath)
        except:
            pass

print('Done!')
print('Removing temporary directories...')
try:
    shutil.rmtree(path=extractPath)
except:
    pass
print('Done!')
print('Extracted icons are in icons folder!')
