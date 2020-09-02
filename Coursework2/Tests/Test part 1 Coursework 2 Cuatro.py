ranges = [[53,57],[42,43],[58,63]]
result =['','']
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]
properties = []

def DiamondQuality (properties):
    
    for i in range (len (properties)):
        i = str(properties [i])
        print (i)          
        if i.isalpha():
            result [0] = feedback [2]
            print (result)
            return result
          

        elif len (properties) != 3:
            result [0] = feedback [1]
            print (result)
            return result
       
             
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
    return (result)



def main ():
    j = 0
    while 'q' not in properties and result [1] != outcomes [1]:
        table =  (input ('Introduce table value: ',))
        properties.append (  (table))
        pavillion =  (input ('Introduce pavillion: ',))
        properties.append ( (pavillion))
        length =  (input ('Introduce length value: ',))
        properties.append ((length))   

        DiamondQuality(properties)
        
        for i in range (len (properties)):
            properties.pop ()
       

        
        
        j = j + 1

main ()
