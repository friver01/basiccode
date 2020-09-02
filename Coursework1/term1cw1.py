#Place Plagiarism statement here

# I have read and understood the sections of plagiarism in the College Policy on
# assessment offences and confirm that the work is my own, with the work of others
# clearly acknowledged. I give my permission to submit my work to the plagiarism
# testing database that the College is using and test it using plagiarism detection
# software, search engines or meta-searching software.

#Place you name and course details here

# Francisco Rivero. Student number: 13183641 MSc Information Systems and Management 02/11/2019




#1) Refactor the following conditional without using any boolean operators (note: this will increase the number of branches)
# 4 marks

# We ask the user to input units and speed. The format remains the same.
units = input("please input units, either mph or km/h ")
speed = int(input("please input your speed as a whole number "))

# We have to extend the number of branches to avoid Boolean operators. 
if (units =='mph'):
    if speed > 70:
        print ('Too Fast')
    else:
        print ('OK')

#Now we consider km/h. In both programs there is a caveat: there is not control of the units input veracity 

elif (units == 'km/h'):
    if (speed > 105):
        print ('Too Fast')
    else:
        print ('OK')

# I add this else operator to get the same outcome than the original program in case of error in the unit input. Ideally we should add a
# veracity control in both programs.

else:
    print ('OK')




#2) Refactor the following code to reduce the number of  branches.
# A program that is short but gives the incorrect output will be given fewer marks than a program that is longer but gives the correct output.
# 8 marks

#We ask for the input. The format remains the same. There is not input veracity. In case of Wrong input the output will be 'Not Ok' in both. 

a = input("please input y or n or c: ")
b = input("please input y or n or c: ")

# Out of the nine possibilities combining the potential input there are 4 OK (always when a==n (3) and when a==y and b==c (1))

if ((a == 'y') and (b == 'c')) or (a=='n'):
    output = 'OK'

# there are 5 'not OK' combinations plus everytime that there is an error in the input (for both variables). In these cases it is 'Not OK'
# I use the operator else to group them all.

else:
    output = 'Not OK'

print (output)


     
#3)  Write your program below. 35 marks.

# Set standard measurements to enable the quality assessment. I use strings instead of integers to facilitate the isdigit validation and
# because we do not have to operate with these measures. I use capital letters because they are fixed values.

MINTABLE = '53'
MAXTABLE = '57'
MINPAVILLION = '42'
MAXPAVILLION = '43'
MINDEPTH = '58'
MAXDEPTH = '63'

# Call functions to input diamond measures

table = (input ('Please enter the table (as a percentage) of your diamond:   ' , ))           
pavillion = (input ('Please enter the pavillion (as a percentage) of your diamond:   ' , ))
depth = (input ('Please enter the depth (as a percentage) of your diamond:  ',))

# Error message in case of no whole number. isdigit is applied on a string.

if not (table.isdigit () and pavillion.isdigit() and depth.isdigit ()) :
    print ('You have entered at least one input incorrectly')
  

# If the output is valid, I compare diamond measures to standards. I could have used AND operator changing the signs of the comparisons
# to identify good diamonds and print not diamond in the else operator by default.

else:
    if ((table < MINTABLE) or (table > MAXTABLE)):
        print ('This is a bad diamond')

    elif ((pavillion < MINPAVILLION) or (pavillion > MAXPAVILLION)):
        print ('This is a bad diamond')
    
    elif ((depth < MINDEPTH) or (depth > MAXDEPTH)):
        print ('This is a bad diamond')

    else:
        print ('This is a good diamond')
