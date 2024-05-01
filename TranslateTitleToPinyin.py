from pypinyin import Style, lazy_pinyin
 
def to_pinyin(originText):
    translatedText = ''.join(lazy_pinyin(originText, style=Style.NORMAL))
    print("Translate '"+originText+"' to '"+translatedText+"'.")
    return translatedText

#测试
#print(to_pinyin('007:qg中文'))