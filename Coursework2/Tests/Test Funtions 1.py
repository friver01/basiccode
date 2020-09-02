

def cubeVolume (sideLenght):
    volume = sideLenght ** 3
    return volume


sideLenght = int(input ('Introduce sideLenght:', ))

while sideLenght >= 0:
    print (cubeVolume (sideLenght))
    sideLenght = int(input ('Introduce sideLenght:', ))
