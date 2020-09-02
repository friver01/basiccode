def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0] 


mystr = "ab"

print("The Given String  is: ", mystr)

print("Reversed String is: ", reverse(mystr)+mystr)

reverse (mystr)

