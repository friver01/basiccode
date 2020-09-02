def ProcessBatch(filename):
    inputFileName = input ('Input file: ')
    filenameinput = (str(filename) + '.dat')
    filenameoutput = (str(filename) + 'out.dat')


    inputFile = open (filenameinput, 'w')
    except IOError:
        print ('Could not process file')
    outputFile = open (filenameinput, 'w')
    except IOError:
        print ('Could not process file')

# As I do not have to finish the exercise by the deadline, I explain the steps:
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

 #ProcessQuery (gemInstitute, properties)
 #ProcessBatch (filename)
    

main()
