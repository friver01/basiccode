def boxString (contents):
    n = len (contents)
    if n == 0:
        return
    print ('-'* (n+2)) 
    print ('!' + contents + '!')
    print ('-'* (n+2))

contents = input ('Write a word:',)
boxString (contents)
