def DiamondQuality(properties):
    
    check = ''
    for i in range (len (properties)):
        check = check + properties [i] 
   
    if len (properties) != 3:
        result [0] = feedback [1]
        print (result)
        return result

    elif not check.isdigit ():
        result [0] = feedback [2]
        print (result)
        return result

    else:
        for i in range (len (properties)):
            print (int (properties[i]))
            if ranges [i][1] >= int(properties[i]) >= ranges [i][0] :
                result [0] = feedback [0]
                result [1] = outcomes [1]
            else:
                result [0] = feedback [0]
                result [1] = outcomes [0]
                print (result)
                return result

    print (result)
    return result
        
       

ranges = [[53,57],[42,43],[58,63]]
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]
    # use the lists with loops to simplify your code

result =['','']
properties = []

properties = ['57','42','60']
DiamondQuality (properties)
