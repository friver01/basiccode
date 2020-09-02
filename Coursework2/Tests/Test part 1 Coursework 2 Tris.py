ranges = [[53,57],[42,43],[58,63]]
result =['','']
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]
properties = ['58','43','56']

def DiamondQuality (properties):
    
    for i in range (len (properties)):
        i = str(properties [i])
        print (i)          
        if i.isalpha():
            result [0] = feedback [2]

        elif len (properties) != 3:
            result [0] = feedback [1]
             
        else:
            for i in range (len(properties)):
                print (i)
                if ranges [i][0] <= int(properties[i]) <= ranges [i][1] :
                    result [0] = feedback [0]
                    result [1] = outcomes [1]
                else:
                    result [0] = feedback [0]
                    result [1] = outcomes [0]    

    print (result)
    return result


DiamondQuality(properties)
