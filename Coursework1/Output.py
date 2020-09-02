a = input("please input y or n or c: ")
b = input("please input y or n or c: ")
if a=="y":
    if b == "c":
        output ="OK"
    else:
        output = "Not OK"

elif a == "n":
    if b == "y":
        output ="OK"
    elif b == "n":
        output ="OK" 

    else:
        output = "OK"

else:
    output = "Not OK"

print(output)


a = input("please input y or n or c: ")
b = input("please input y or n or c: ")

if ((a == 'y') and (b == 'c')) or (a=='n'):
    output = 'OK'

else:
    output = 'Not OK'

print (output)
