#Place Plagiarism statement here
#I have read and understood the sections of plagiarism in the College Policy
#on assessment offences and confirm that the work is my own, with the work of 
#others clearly acknowledged. I give my permission to submit my work to the 
#plagiarism testing database that the College is using and test it using plagiarism
#detection software, search engines or meta-searching software.

#Place you name and course details here

# Francisco Rivero MSc Information Systems and Management Student Id: 13183641
# Submitted 2020/04/10



class Person:
    def __init__(self, name, age):
        #Creates two instance variables
        #name is a string
        self._name = name
        #age is an integer
        self._age = age
        #Implement this method
        

    def getName(self):
        #Returns the name of the person
        return self._name
        #Implement this method
        

    def getAge(self):
        #Returns the age of the person
        return self._age
        #Implement this method
        
    
    def __repr__(self):
        #Display the data in the following format 
        #Name:  then print the name
        #    Age: then the age
        #Implement this method
        return 'Name: %s\n    Age: %d' % (self._name, self._age)


class Student(Person):
    #implement this class
    pass

def DisplayAllDetails(people):
    #implement this function
    pass

def DisplayNameWithAge(people,age):
    #implement this function
    pass

    
def TestPerson():
    p = Person("Alex",20)
    print(p)
    print("******")
    print(p.getName())
    print(p.getAge())

def TestStudent():
    s = Student("Keith",30, "Computing")
    print(s)
    print("******")
    print(s.getName())
    print(s.getAge())
    
def TestFunctions():
    people = [Person("Alex",20), Student("Keith",30, "Computing"), Person("Petra",40), Person("John",30)]
    DisplayAllDetails(people)
    print("******")
    DisplayNameWithAge(people,30)
