#Place Plagiarism statement here

#I have read and understood the sections of plagiarism in the College Policy
#on assessment offences and confirm that the work is my own, with the work of 
#others clearly acknowledged. I give my permission to submit my work to the 
#plagiarism testing database that the College is using and test it using plagiarism
#detection software, search engines or meta-searching software.

#Place you name and course details here

# Francisco Rivero MSc Information Systems and Management Student Id: 13183641
# Submitted 2020/02/21

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


# Open the input file. As the input is given in a string I add .dat extension file

    CompleteFileName = (str(sName) + '.dat')
#    print (CompleteFileName)

   
    inputFile = open (CompleteFileName, 'r')


    for line in inputFile:
        line = line.rstrip() # Removes the space at the end
        fields = line.split (',') # Split the line considering ','

        if len (fields) == 3:   # To differentiate measures from outcomes
            defproperty = fields [0]
            propertyNames.append (defproperty)
            defrangesmin= float(fields [1])
            rangesmin.append (defrangesmin)
            defrangesmax= float(fields [2])
            rangesmax.append (defrangesmax)        

        else:
            if fields [0] != SEPARATOR: # Considers the outcome and excludes SEPARATOR
                defoutcomes = fields [0]
                outcomes.append (defoutcomes)

    for i in range(0, len(rangesmin)):  # I use this loop to build the elements of the range table based on rangemax and rangemin
        srange = [rangesmin [i], rangesmax [i]]
        ranges.append (srange)


    variables = (outcomes, propertyNames, ranges)

#    print (outcomes)    
#    print (propertyNames)
#    print (ranges)
#    print (variables)

    return (outcomes, propertyNames, ranges)

    CompleteFileName.close()





#Q2  
def GetFeedback(outcomes, propertyNames, ranges, properties):


    failedProperties = []

    feedback = ["Inputs are all valid", "The number of properties must be equal to the range","At least one input is incorrect"]
    # use the lists with loops to simplify your code. I will use it in #Q3

    if len(properties) != len(ranges):
        return [feedback[1],"",'']

    bValid = True
    for n in properties:
        bValid = bValid and n.isdigit()

    if not bValid:
        return [feedback[2],"",'']

    bGood = True
    
    for id in range (len(properties)):
        iproperty = int(properties [id])
        if iproperty < ranges[id][0] or iproperty > ranges[id][1]:
            failedProperties.append (propertyNames [id])

#    print (failedProperties)


    if failedProperties != [] :
        bGood = False
        return [feedback [0], outcomes[1],failedProperties]

    else:
        return [feedback [0], outcomes[0],failedProperties]
        	


	
#Q3 	
def ProcessQuery(gemInstitute, properties):

    # I add a list with the outcomes suggested in the exercise
    feedback2 = ["Inputs are all valid", 'Inputs are not valid' "Number of input values do not match the number of properties","At least one input is incorrect",'Data for this Institute not currently available']

    # As there are variables defined in other functions I have the define them again inside the function

    parameters = LoadData (gemInstitute)
    propertyNames = parameters [1]
    outcomes = parameters [0]
    ranges = parameters [2]
    parameters1 = GetFeedback(outcomes, propertyNames, ranges, properties)
    sname = (str(gemInstitute) + '.dat')
    failedProperties = parameters1[2]


    import os 
    while not os.path.exists (sname):
        return ['Data for this institute not currently available','']

    if len(properties) != len(ranges):
        return [feedback2[2],'']

    bValid = True
    for n in properties:
        bValid = bValid and n.isdigit()

    if not bValid:
        return [feedback2[1],'']

       
    if failedProperties == [] :
        return [feedback2 [0], parameters1[0], parameters1 [1]]

#Q4

def ProcessBatch(filename):
    inputFileName = input ('Input file: ')
    filenameinput = (str(filename) + '.dat')
    filenameoutput = (str(filename) + 'out.dat')


    try:
        inputFile = open (filenameinput, 'w')
    except IOError:
        print ('Could not process file')
        
    try:
        outputFile = open (filenameinput, 'w')
    except IOError:
        print ('Could not process file')

# As I have run out of time to submit the exercise by the deadline, I explain the theoretical steps:
# Firstly we have to produce the strings to be added in the different files:
    # File 1 Batch.dat: adding a list to the existing file
    # To produce the string we consider: a) User Id: I have to input manually b) gemInsititute
    # (it can be easily taken from LoadData) and c) Properties (it is a variable already
    # considered in the exercise. Once I have generated the list, i can add it as a string with
    # batch.write (string)

    # File 2 Batchout.dat In this case we have to a) User id: we have to input manually
    # b) the rest of the string to be added is the return of the ProcessQuery function. Once i have
    # generated the list I can added with batchout.write (string)

# For simplicity I would consider GetFeedback function for adding strings in batch.dat and ProcessQuery
# function for adding outcomes.Everytime I am running one of the previous functions
# I would add a list with the previous components using the command f.write (string)

# Finally, I would close the files
    infile.close()
    outfile.close()

        
# I have added this main function to execution the previous ones. Instead of writing
# data directly in the function I have added some lines to input 





def main ():

    # Check files in the directory

    import os

    contents = os.listdir()
    print (contents)

    # Prompt for the input file name

    gemInstitute = input ('Input file: ')
    sname = (str(gemInstitute) + '.dat')
#    print (sname)

    while not os.path.exists (sname):
        print ('Data for this institute not currently available')
        gemInstitute = input ('Input file: ')
        sname = (gemInstitute + '.dat')

    LoadData (gemInstitute)

    parameters = LoadData (gemInstitute)
    propertyNames = parameters [1]
    outcomes = parameters [0]
    ranges = parameters [2]

       # use this list to simplify your code
    bEnd = False
    while not bEnd:
        properties = []
        for name in propertyNames:
            properties.append(input("Please input, "+ name + " "))

        if "q" in properties:
            bEnd = True
        else:
            ret = GetFeedback(outcomes, propertyNames, ranges, properties)
            if ret[0] == "Inputs are all valid":
                print (ret[1],ret[2])
                bEnd = True
            else:
                print(ret[0])

#   ProcessQuery (gemInstitute, properties)
#   ProcessBatch (filename)
    

main()



