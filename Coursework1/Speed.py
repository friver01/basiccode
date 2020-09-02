# Refactor (see Question 5 on lab sheet 4 for the deﬁnition of refactor) the conditional statement in the following program
#without using any boolean operators (note: this will increase the number of branches).

units = input("please input units, either mph or km/h ")
speed = int(input("please input your speed as a whole number "))

if (units == "mph" and speed > 70) or (units == "km/h" and speed > 105):
    print("Too Fast")
else:
    print("OK")

units = input("please input units, either mph or km/h ")
speed = int(input("please input your speed as a whole number "))

if (units =='mph'):
    if speed > 70:
        print ('Too Fast')
    else:
        print ('OK')
        

elif (units =='km/h'):
    if (speed > 105):
        print ('Too Fast')
    else:
        print ('OK')

else:
    print ('OK')
    
