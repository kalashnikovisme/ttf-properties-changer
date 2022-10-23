import xml.etree.ElementTree as ET
file = '/usr/share/MartianMono-CnBd.ttx'
tree = ET.parse(file)
tree.find('/post/isFixedPitch').set('value', '1')
tree.write(file)
