def ExpandCenterit (text):
    text2 = ''
    for i in text:
        text2 = i + text2 + i 
    return text2

text = 'abc'
print (ExpandCenterit (text))
