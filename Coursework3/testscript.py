# Simple Unit testing script which runs functions of code
# for which the correct answer is known.


from Term2cw1 import *

(outcomes, propertyNames, ranges) = LoadData("PGS")

if outcomes == ['Excellent Ideal cut', 'Not Excellent Ideal cut'] :
    print("Step 1 Success! - outcomes")
else:
    print("Step 1 Failed - outcomes")

if propertyNames == ['Table width', 'Crown Height', 'Crown Angle', 'Pavilion Depth', 'Pavilion Angle']:
    print("Step 1 Success! - property names")
else:
    print("Step 1 Failed - property names")

if ranges == [[53.0, 57.0], [14.0, 16.5], [33.5, 35.5], [42.5, 44.0], [40.5, 41.0]]:
    print("Step 1 Success! - ranges")
else:
    print("Step 1 Failed - ranges")


(outcomes, propertyNames, ranges) = (['Excellent Ideal cut', 'Not Excellent Ideal cut'], ['Table width', 'Crown Height', 'Crown Angle', 'Pavilion Depth', 'Pavilion Angle'], [[53.0, 57.0], [14.0, 16.5], [33.5, 35.5], [42.5, 44.0], [40.5, 41.0]]) 
(outcome, badProperties)=GetFeedback(outcomes, propertyNames, ranges,[53.1,14.2,33.5,42.5,41.5])

if outcome == 'Not Excellent Ideal cut':
    print("Step 2 Success! - Outcome")
else:
    print("Step 2 Failed - Outcome")

if badProperties == ['Crown Angle', 'Pavilion Depth']:
    print("Step 2 Success! - Bad Properties")
else:
    print("Step 2 Failed - Bad Properties")

if ProcessQuery("PGS",[53.1,14.2,33.5,42.5,41.5]) ==  ('Inputs are all valid', ('Not Excellent Ideal cut', ['Crown Angle', 'Pavilion Depth'])):
    print("Step 3 Success!")
else:
    print("Step 3 Failed")

