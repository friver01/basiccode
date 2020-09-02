#Place Plagiarism statement here

#I have read and understood the sections of plagiarism in the College Policy
#on assessment offences and confirm that the work is my own, with the work of 
#others clearly acknowledged. I give my permission to submit my work to the 
#plagiarism testing database that the College is using and test it using plagiarism
#detection software, search engines or meta-searching software.

#Place you name and course details here

# Francisco Rivero MSc Information Systems and Management Student Id: 13183641
# Submitted 2020/01/10



#1a)
    
ranges = [[53,57],[42,43],[58,63]]
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]
    # use the lists with loops to simplify your code

# I add two lists: result is a list with 2 strings as requested. Both are empty until replaced when calling the function.


result =['','']
# I add this list with 2 strings as requested. Both are empty until replaced when calling the function.


## We define the Function with one argument as requested
# One single argument that contains a list of 3 elements
# I validate the argument comparing with the table ranges
# Returns a list with 2 elements



def DiamondQuality(properties):
    

    # Loop to generate one string based on the different elements added to properties

    check = ''
    for i in range (len (properties)):
        check = check + properties [i] 
   
    # Validation of properties list length (useful when elements are added manually as in 1a)

    if len (properties) != 3:
        result [0] = feedback [1]
        result [1] = ''
        return result

    #Entry validation using isdigit to previous string to check user entries are numbers
    
    elif not check.isdigit ():
        result [0] = feedback [2]
        result [1] = ''
        return result


    # If conditions regarding length and format are met. I use a loop to compare every element of the properties list with the parameters   
    # included in the table ranges. If one of the properties does not meet the range I finish the loop with return.
    # I fill in the 2 strings of the function depending on the result

    else:
        for i in range (len (properties)):
            if ranges [i][1] >= int(properties[i]) >= ranges [i][0] :
                result [0] = feedback [0]
                result [1] = outcomes [1]
            else:
                result [0] = feedback [0]
                result [1] = outcomes [0]
                return result

    return result
        
# I add the 3 elements of the argument properties manually. In exercise 1b) I will replace these values with the user inputs
       
properties = ['53','10','60']
print (DiamondQuality (properties))




#1b)

## We use this main function as requested.
# Firstly I empty the previous content to continue continue aplying the previous function to the 3 given elements.
# I include an loop using while because the iteration occurs until one of the both conditions happen.

def main():
    inputProperties = ["table", "pavillion", "depth"]
    # use this list to simplify your code
    
    j = 0
    # sentinel of while loop

    while 'q' not in inputProperties and result [1] != outcomes [1]:
    # iteration plus 2 conditions to end 
 
        for i in range (len (inputProperties)):
            # I use a loop to empty the previous elements in the list
            inputProperties.pop ()

        # Input of user data using append to populate the inputProperties list.
        table =  (input ('Introduce table value: ',))
        inputProperties.append (table)
        pavillion =  (input ('Introduce pavillion: ',))
        inputProperties.append (pavillion)
        depth =  (input ('Introduce length value: ',))
        inputProperties.append (depth)

        # Calls previous function and prints the outcome.
 
        print (DiamondQuality(inputProperties))     

        j = j + 1

## Calls the main function
        
main ()



#Put your answers to the remaining questions here:

##2 Repeat each letter in a string without using recursion.
# @param text the text to update.
# @return string containing the doubled letters. 

def Expandit (text):
    text1 = ''
    for i in text:
        text1 = text1 + i + i
    return text1

def main ():
    # Demonstrates the fuction
    word = input ('Introduce text to duplicate reapeating each letter: ', )
    print ('Duplicated text is: ', Expandit(word))

# Calling main function
main ()

##3a Duplicate a string placing first character in the center and rest at the sides using without recursion

def ExpandCenterit (text):
    text2 = ''
    for i in text:
        text2 = i + text2 + i 
    return text2

def main ():
    # Demonstrates the funcion
    word = input ('Introduce text to duplicate and reverse: ', )
    print ('Duplicated and Reversed text is: ', ExpandCenterit (word))

# Call main function
main ()


##3b Duplicate a string placing first character in the center and rest at the sides using recursion

def duplicatereverse(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + duplicatereverse(text[0:-1]) + text[-1]
    

def main():
    # Demonstrates the funcion
    word = input ('Introduce text to duplicate and reverse: ', )
    print('Duplicated and Reversed text is: ', duplicatereverse(word))

# Call the main function

main()


