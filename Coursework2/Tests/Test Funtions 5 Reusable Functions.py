# This program demonstrates a reusable function

def main():
    print ('Please enter a time: hours, then minutes')
    hours = readIntBetween (0,23)
    minutes = readIntBetween (0,59)
    print ('You entered %d hours and %d minutes.' % (hours, minutes))


def readIntBetween (low, high):
    value = int (input ('Enter a value between' + str(low) + 'and' + str (high) + ':'))
    while value < low or value > high:
        print ('Error: value out of range')
        value = int (input ('Enter a value between' + str(low) + 'and' + str (high) + ':'))
    return value
           
main()
