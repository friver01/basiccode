
def Expandit (text):
    text2 = ''
    for i in text:
        text2 = i + text2 + i 
    return text2

def Expandit1 (text):
    if len (text) > 10: return
    Expandit1 (text + text [0])

text = 'abcd'

Expandit (text)
     

text = 'abcd'
print (len(text))
print (Expandit (text))
print (Expandit1 (text))
