import sys
sys.path.append(r"Z:\\My CodingWorks\\Workspace")

from JellyfinSortTitleAutoFilling.ListNFOFile import find_files_with_suffix
from JellyfinSortTitleAutoFilling.ReadNFOFile import Read_NFO_tag_value
from JellyfinSortTitleAutoFilling.TranslateTitleToPinyin import to_pinyin
from JellyfinSortTitleAutoFilling.UpdateNFOFile import write_NFO_tag_value

# 指定的电影或者电视文件夹，目标找到里面包含的所有.nfo文件
directory_path = "G:\\My Movies"
suffix = '.nfo'
files = find_files_with_suffix(directory_path, suffix)


# 指定读取标签名称
readTagName = 'title'
# 指定读取标签值
readTagValue = ''
# 指定写入标签名称
writeTagName = 'sorttitle'
# 指定写入标签值
writeTagValue = ''

"""
遍历所有.nfo文件
读取title标签值, 即电影或电视墙显示的电影或电视名称
中文翻译成拼音字符串
把译文写入sorttitle标签, 插入或者覆盖
"""
for file in files:
    print("###")
    print("---Start to update .nfo file '"+file+"'")
    readTagValue = Read_NFO_tag_value(file,readTagName)
    writeTagValue = to_pinyin(readTagValue)
    write_NFO_tag_value(file,writeTagName,writeTagValue)
    print("---Complete updating .nfo file '"+file+"'")
    print("@@@")
