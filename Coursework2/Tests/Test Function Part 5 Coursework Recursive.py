def Expandit1 (str):
    if len (str) == 0: return (str)

    else:
        return Expandit1 (text[j-1] + str)

    

text = 'abcd'
j = len(text)

print (Expandit1 (text))
