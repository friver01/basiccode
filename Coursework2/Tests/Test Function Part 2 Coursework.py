def Expand (text):
    text1 = ''
    for i in text:
        text1 = text1 + i + i
    return text1




def Expandit (text):
    text2 = ''
    for i in text:
        text2 = i + text2 + i 
    return text2


text = 'abcd'
print (Expand (text))
print (Expandit (text))

def Expand1(text):
    if len(text) == 0:
        text [0] = ''
        return text [0] 

    else:
        return text[0] + text[0] + Expand1(text[1 : ])

print (Expand1 (text))
