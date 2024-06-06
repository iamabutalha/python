



def common_end(a, b):
    """Check array of ints if both have 1 or 3
    at start or end return true or false otherwise"""
    for i in range(len(a)):
        if a[0] == 1 and b[0] == 1:
            return True
        elif a[len(a)-1] == 3 and b[len(b) - 1] == 3:
            return True
        
    return False
      

print(common_end([1, 2, 3], [7, 3])) #→ True 
print(common_end([1, 2, 3], [7, 3, 2])) #→ False
print(common_end([1, 2, 3], [1, 3])) #→ True
print(common_end([2],[2])) #→ False