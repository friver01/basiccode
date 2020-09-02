def LoadData (sName):

# Define the lists where we will be appending values:

    outcomes = []
    propertyNames = []
    ranges = []
    SEPARATOR = '----------'

    rangesmin = []
    rangesmax = []


# Open the input file. Firstly, I convert the string into a .dat file

    CompleteFileName = (str(sName) + '.dat')
    print (CompleteFileName)

    #while not os.path.exists (CompleteFileName):
     #   print ('Error: file name not found')
      #  inputFileName = input ('Input file: ')
       # sname = (CompleteFileName + '.dat')
        #print (CompleteFileName)
    
    inputFile = open (CompleteFileName, 'r')


    for line in inputFile:
        line = line.rstrip() # Removes the space at the end
        fields = line.split (',')

    # I split into 3 different files where there are 3 components in the line and add them to their list

        if len (fields) == 3: 
            defproperty = fields [0]
            propertyNames.append (defproperty)
            defrangesmin= float(fields [1])
            rangesmin.append (defrangesmin)
            defrangesmax= float(fields [2])
            rangesmax.append (defrangesmax)        

    # If there are not 3 components I consider only the first one (except the SEPARATOR) and add the to their list
        else:
            if fields [0] != SEPARATOR:
                defoutcomes = fields [0]
                outcomes.append (defoutcomes)
                
    # I built a table with the different max and min ranges

    for i in range(0, len(rangesmin)): 
        srange = [rangesmin [i], rangesmax [i]]
        ranges.append (srange)

    print (outcomes)    
    print (propertyNames)
    print (ranges)



    return(outcomes, propertyNames, ranges)



    CompleteFileName.close()


# Check files in the directory so they can help me to identify the file

import os

contents = os.listdir()
print (contents)

# Prompt for the input file name

#inputFileName = input ('Input file: ')
#sname = (str(inputFileName) + '.dat')
#print (sname)

#while not os.path.exists (sname):
 #   print ('Error: file name not found')
  #  inputFileName = input ('Input file: ')
   # sname = (inputFileName + '.dat')
    #print (sname)


def GetFeedback(outcomes, propertyNames,ranges,inputProperties):
    

    LoadData ('PgS')

    
    feedback = ["Inputs are all valid", "The number of properties are not equal","At least one input is incorrect"]
    # use the lists with loops to simplify your code

    if len(inputProperties) != len(ranges):
        return [feedback[1],""]

    bValid = True
    for n in inputProperties:
        bValid = bValid and n.isdigit()

    if not bValid:
        return [feedback[2],""]

    bGood = True

    for id in range(len(inputProperties)):
        iproperty = int(inputProperties[id])
        if iproperty < ranges[id][0] or iproperty > ranges[id][1]:
            bGood = False    

    return [feedback[0],outcomes[int(bGood)]]

def main():
    inputProperties = ["table", "pavillion", "depth"]
    # use this list to simplify your code
    bEnd = False
    while not bEnd:
        properties = []
        for name in inputProperties:
            properties.append(input("Please input, "+ name + " "))

        if "q" in properties:
            bEnd = True
        else:
            ret = DiamondQuality(properties)
            if ret[0] == "Inputs are all valid":
                print(ret[1])
                bEnd = True
            else:
                print(ret[0])





