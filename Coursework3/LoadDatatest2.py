## LoadData Function
# Read the EGL and RGS files

def LoadData (sName):

# Define the lists where we will be appending values:

    outcomes = []
    propertyNames = []
    ranges = []
    SEPARATOR = '----------'

    rangesmin = []
    rangesmax = []


# Open the input file

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

        if len (fields) == 3:
            defproperty = fields [0]
            propertyNames.append (defproperty)
            defrangesmin= float(fields [1])
            rangesmin.append (defrangesmin)
            defrangesmax= float(fields [2])
            rangesmax.append (defrangesmax)        

        else:
            if fields [0] != SEPARATOR:
                defoutcomes = fields [0]
                outcomes.append (defoutcomes)

    for i in range(0, len(rangesmin)): 
        srange = [rangesmin [i], rangesmax [i]]
        ranges.append (srange)


    variables = (outcomes, propertyNames, ranges)

    print (outcomes)    
    print (propertyNames)
    print (ranges)
    print (variables)




	#Complete this function for Q1
	# You may add any helper functions you wish
	


    return variables

    CompleteFileName.close()


# Check files in the directory

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

LoadData ('PGS')
