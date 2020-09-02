def Expandit1 (text):
    while len (text) < 2*j: 
        Expandit1 (text[j-1] + text)
        
    print (text)
    return
 

text = 'abcd'
j = len(text)

Expandit1 (text)
