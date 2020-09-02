
# Set standard measurements to enable the quality assessment

MINTABLE = '53'
MAXTABLE = '57'
MINPAVILLION = '42'
MAXPAVILLION = '43'
MINDEPTH = '58'
MAXDEPTH = '63'

# Call functions to input diamond measures

table = (input ('Table measures are:   ' , ))           
pavillion = (input ('Pavillion measures are:   ' , ))
depth = (input ('Depth measures are:  ',))

# Error message in case of no whole number

if not (table.isdigit () and pavillion.isdigit() and depth.isdigit ()) :
    print ('You have entered at least one input incorrectly')
  

# Compare diamond measures to standards

else:
    if ((table < MINTABLE) or (table > MAXTABLE)):
        print ('This is a bad diamond')

    elif ((pavillion < MINPAVILLION) or (pavillion > MAXPAVILLION)):
        print ('This is a bad diamond')
    
    elif ((depth < MINDEPTH) or (depth > MAXDEPTH)):
        print ('This is a bad diamond')

    else:
        print ('This is a good diamond')
    

  

