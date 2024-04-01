import sys

try:
     z = int(input("Enter Value of X: "))
     y = int(input("Enter Value of Y: "))

except ValueError:
    print("Enter Integer not String ")
    sys.exit(1)


#try:
if z < y:
    print("z is less than y ")
elif z > y:
    print("z is greater than y ")
else:
    print("z is equal to Y ")        
#except NameError:
  #  print("VAlue cannot be campare ") 
   # sys.exit(1)       