import xml.etree.ElementTree as ET
import sys

file = sys.argv[1]
xmlFile = open(file, 'r')
firstLine = xmlFile.readline()
tree = ET.parse(file)
tree.find('/post/isFixedPitch').set('value', '1')
tree.write(file)

xmlFile = open(file)
text = xmlFile.read()
xmlFile.close()

xmlFile = open(file, 'w')
xmlFile.write(firstLine)
xmlFile.write(text)
xmlFile.close()
