
properties = ['57','45','60']

check = ''
for i in range (len (properties)):
    check = check + properties [i] 

print (check)

checkalfanumericentries = properties [0]+properties [1]+properties[2]
print (checkalfanumericentries)

if checkalfanumericentries.isdigit():
    print ('true')

else:
    print ('false')
