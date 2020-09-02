def pyramidVolume (height, baseLenght):
    baseArea = baseLenght * baseLenght
    return height * baseArea / 3


def main ():
    height = int (input ('Introduce height:',))
    baseLenght = int (input ('Introduce baseLenght',))
    print (pyramidVolume (height,baseLenght))

print ('Hello')

main()
 


