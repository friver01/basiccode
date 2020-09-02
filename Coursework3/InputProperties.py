


def DiamondQuality(properties):

    ranges = [[53.0, 57.0], [14.0, 16.5], [33.5, 35.5], [42.5, 44.0], [40.5, 41.0]]
    outcomes = ['Excellent Ideal cut', 'Not Excellent Ideal cut', '']
    propertyNames = ['Table width', 'Crown Height', 'Crown Angle', 'Pavilion Depth', 'Pavilion Angle']

    failedProperties = []

    feedback = ["Inputs are all valid", "The number of properties must be equal to the range","At least one input is incorrect"]
    # use the lists with loops to simplify your code

    if len(properties) != len(ranges):
        return [feedback[1],"",'']

    bValid = True
    for n in properties:
        bValid = bValid and n.isdigit()

    if not bValid:
        return [feedback[2],"",'']

    bGood = True
    
    for id in range (len(properties)):
        iproperty = int(properties [id])
        if iproperty < ranges[id][0] or iproperty > ranges[id][1]:
            failedProperties.append (propertyNames [id])

    print (failedProperties)


    if failedProperties != [] :
        bGood = False
        return [feedback [0], outcomes[1],failedProperties]

    else:
        return [feedback [0], outcomes[0],failedProperties]
        


def main():
    propertyNames = ['Table width', 'Crown Height', 'Crown Angle', 'Pavilion Depth', 'Pavilion Angle']
    # use this list to simplify your code
    bEnd = False
    while not bEnd:
        properties = []
        for name in propertyNames:
            properties.append(input("Please input, "+ name + " "))

        if "q" in properties:
            bEnd = True
        else:
            ret = DiamondQuality(properties)
            if ret[0] == "Inputs are all valid":
                print (ret[1],ret[2])
                bEnd = True
            else:
                print(ret[0])

        

main()
