characters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,zip]
digits = [0,1,2,3,4,5,,6,7,8,9]
symbols = [¬,!,£,$,%,^,&,*,(,),_,+]
          

from random import randint:

def randomCharacter (characters):
    n

def makePassword (lenght):
    password = ''
    for i in range (lenght - 2):
        password = password + randomCharacter ('abcdefghijklmnopqrstuvwxyz')

    randomDigit = randomCharacter ('0123456789')
    password = insertAtRandom (password, randomDigit)

    randomSymbol = randomCharacter ('+!"£$%')

    return password

def main():
    value = int (input ('Introuduce lenght:',))
    print (makePassword (value))


print ('Hello')

main ()
    
