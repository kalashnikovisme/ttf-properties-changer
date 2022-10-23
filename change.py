import xml.etree.ElementTree as ET
import sys

file = sys.argv[1]
key = sys.argv[2]
attribute = sys.argv[3]
value = sys.argv[4]
xmlFile = open(file, 'r')
firstLine = xmlFile.readline()
tree = ET.parse(file)
tree.find(key).set(attribute, value)
tree.write(file)

xmlFile = open(file)
text = xmlFile.read()
xmlFile.close()

xmlFile = open(file, 'w')
xmlFile.write(firstLine)
xmlFile.write(text)
xmlFile.close()
