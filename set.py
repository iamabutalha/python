import sys
s = set()

# In set number is just shown one duplicate values are Ignored
try:
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(1)



    print(s)

    s.remove(4)

    print(s)

except KeyError:
    print("Value is not in set ")
    sys.exit(1)