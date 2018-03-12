# coding=utf-8
# @File  : main.py
# @Author: PuJi
# @Date  : 2018/3/12 0012

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print root.tag
print root.attrib

for child in root:
    print (child.tag, child.attrib)