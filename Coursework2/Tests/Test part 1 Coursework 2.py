ranges = [[53,57],[42,43],[58,63]]
outcome =['','']
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]


properties =[]
table =  (input ('Introduce table value: ',))
properties.append (  (table))
pavillion =  (input ('Introduce pavillion: ',))
properties.append ( (pavillion))
length =  (input ('Introduce length value: ',))
properties.append ((length))

print (properties)
print (len(properties))

if len (properties) != 3:
    print (feedback [1])

break 

for i in range (len (properties)):
    i = properties [i]
    print (i)
    if i.isalpha():
        outcome [0] = ('At least one digit is incorrect')
        print (feedback[2])
        break 
    else:
        outcome [0] = ('Inputs are valid')


for i in range (len(properties)):
    print (i)
    if ranges [i][0] <= int(properties[i]) <= ranges [i][1]:
        outcome [1] = ('This is a good diamond')
    else:
        outcome [1] = ('The diamond is bad')    

print (outcome)
