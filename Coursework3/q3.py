def ProcessQuery(gemInstitute, properties):
    feedback2 = ["Inputs are all valid", 'Inputs are not valid' "Number of input values do not match the number of properties","At least one input is incorrect",'Data for this Institute not currently available']


    parameters1 = GetFeedback (outcomes, propertyNames, ranges, properties)

    while not os.path.exists (sname):
        return ['Data for this institute not currently available','']

    if len(properties) != len(ranges):
        return [feedback2[2],'']

    bValid = True
    for n in properties:
        bValid = bValid and n.isdigit()

    if not bValid:
        return [feedback2[1],'']

       
    if failedProperties == [] :
        return [feedback2 [0], parameters1[0], parameters1 [1]]
