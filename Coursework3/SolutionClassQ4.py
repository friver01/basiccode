## Coursework number 3 Q4

def ProcessBatch (filename):

    try:
        with open (filename +'.dat','r') as inf:
            with open (filename + 'out.dat') as outf:
                for line in inf:
                    words = line.split (',')
                    (feedback, output) = ProcessQuery (words [1].strip(),
                    outdisplay = ''

                    if feedback == 'Inputs are all valid')
                        if output [1] != []:
                            for i in output [1]:
                                outdisplay = outdisplay + ',' + i
                            print (i)
                        outf.write (words [0] + str (output [0]) + outdisplay + 'n')

                    else:
                        outf.write (words [0] + ',' + feedback + 'n')
                    
    except Exception:
        print ('Could not process file')
    

ProcessBatch ('BatchQueries')
