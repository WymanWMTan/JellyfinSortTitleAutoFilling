import xml.etree.ElementTree as ET
 

def Read_NFO_tag_value(xmlFile, tagName):
    # 加载XML文件
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    #初始化字符串标签值
    tagValue = ''
    
    # 读取特定标签的值
    for elem in root.iter(tagName):
        tagValue = elem.text

    print("Read tag '"+tagName+"' with value '"+tagValue+"'")

    return tagValue
