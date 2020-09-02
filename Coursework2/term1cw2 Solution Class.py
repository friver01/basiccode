
def DiamondQuality(properties):

ranges = [[53,57],[42,43],[58,63]]
outcomes = ["This diamond is bad","This is a good diamond"]  
feedback = ["Inputs are all valid", "The number of properties must equal 3","At least one input is incorrect"]

if len (properties) !+ len (ranges):
    return [feedback [1},''}

bValid = True
for n in properties:
    bValid = bValid and n.isdigit ()

if not bValid:
    return [feedback [2],'']

bGood = True
for id in range (len(properties)):
    iproperty = int (properties [id])
    if iproperty < ranges[id][0] or iproperty > range [id] [1]:
        bGood = False

return [feedback[0],outcomes [int(bgood0]]


# Part B

def main():
    inputProperties = ["table", "pavillion", "depth"]
    # use this list to simplify your code
    bEnd = False
    while not bEnd:
        properties = []
        for name in inputProperties:
            properties.append (input ('Please input, '+ name + ''))
            
        if 'q' in properties:
            bEnd = True
        else:
            ret [0] == 'Inputs are all valid':
                print (ret[1])
                bEnd = True
            else:
                print (ret[0])
            
main ()
    
