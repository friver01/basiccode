# Write a function called ExpandIt that is a refactor of the following code. Your function must not use recursion.
## Repeat each letter in a string.
# @param text the text to update.
# @return string containing the doubled letters.

#def Expand(text):
 #   if len(text) == 0:
  #      text [0] = ''
   #     return text [0] 
    #else:
     #   return text[0] + text[0] + Expand(text[1 : ])

# Hint: what does Expand(’abcd’) return?

#text = 'abcd'

#Expand (text)

text = (input('Introduce text:',)) 

def Expand (text):
    if len (text) == 0:
        text = ''
    else:
        for i in range (len(text)):
            text (i) = text (i) + text (i)
        return text

Expand (text)

print (len (text))
print (text [0])
