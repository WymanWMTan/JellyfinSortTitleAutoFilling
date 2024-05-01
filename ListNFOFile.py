import os
 
def find_files_with_suffix(directory, suffix):
    """
    在指定目录中找到具有指定后缀的所有文件。
    
    :param directory: 要搜索的目录路径。
    :param suffix: 文件后缀。
    :return: 文件列表，包含所有找到的文件的完整路径。
    """
    # 初始化一个空列表来存储找到的文件
    files_with_suffix = []
    
    # 使用os模块的walk函数遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件名是否以指定后缀结束
            if file.endswith(suffix):
                # 将文件的完整路径添加到列表中
                files_with_suffix.append(os.path.join(root, file))
    
    if len(files_with_suffix) > 0:
        print(" Found "+ str(len(files_with_suffix)) +" .nfo files ")
    else:
        print(" No .nfo file found")

    return files_with_suffix