import sys

try:
     x = int(input("Enter Value of X: "))
     y = int(input("Enter Value of Y: "))

except ValueError:
    print("Enter Integer not String ")
    sys.exit(1)


#try:
if x < y:
    print("X is less than y ")
elif x > y:
    print("X is greater than y ")
else:
    print("X is equal to Y ")        
#except NameError:
  #  print("VAlue cannot be campare ") 
   # sys.exit(1)       