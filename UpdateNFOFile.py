from queue import Empty
import xml.etree.ElementTree as ET
 
def write_NFO_tag_value(xmlFile, tagName, tagValue):
    # 加载XML文件
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    # 目标标签值
    newTagValue = ''
    
    # 查找并修改标签值
    for elem in root.iter(tagName):
        elem.text = tagValue
        newTagValue = tagValue
        print("update tag '"+tagName+"' with value: '"+tagValue+"'")
    
    if len(newTagValue) == 0:
        new_element = ET.Element(tagName)
        new_element.text = tagValue
        root.append(new_element)
        print("insert tag '"+tagName+"' with value: '"+tagValue+"'")

    # 保存修改后的XML文件
    tree.write(xmlFile, encoding='utf-8', xml_declaration=True)

    print("update "+xmlFile+" sucessfully")