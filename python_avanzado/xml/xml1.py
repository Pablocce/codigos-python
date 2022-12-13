import xml.etree.ElementTree as ET
path = "C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\xml\1.xml"
#We can import this data by reading from a file:
tree = ET.parse(path)
root = tree.getroot()

print(root.tag)