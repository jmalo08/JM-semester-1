# Worksheet 1.2: Task 1 Solution
import sys
try:
    score = float(input("Enter an integer grade between 0 and 100:"))
except ValueError:
     sys.exit("Error: Grade must be an integer between 0 and 100")


if score.is_integer() == False or score > 100 or score < 0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    
score = int(score)
if score >= 0 and score <=39:
    print(score,"is a Fail")
elif score >= 40 and score <= 69:
    print(score,"is a Pass") 
elif score > 69 and score <=100:
    print(score,"is a Distinction")




