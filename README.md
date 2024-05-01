# JellyfinSortTitleAutoFilling
Python: auto fill "sorttitle" in .nfo file by converting "title" in Chinese characters to Pinyin

# Prerequisite
1. Install Python runtime
2. Install Pypinyin libary: "pip install pypinyin"

# Execution
1. update main.py line 10 with folder path with .nfo files.  eg. "c:\\test\\movie"
2. run main.py

# Result
1. all folders and sub-folders will be scanned for .nfo files
2. read tag "title" from .nfo and convert Chinese Charators into Pinyin alphabet string
3. add or update tag "sorttitle" with the converted string