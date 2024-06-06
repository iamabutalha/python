

from operator import index
from os import replace
from traceback import print_tb

# Replace The word Java with Python
with open("practice.txt", "w") as f:
    data = f.write("I ama the Ai, Machine Learning and Deep Learning Trainer \nI use the Java Language for my projects \nI like programming i Java")
   
with open("practice.txt", "r") as f:
    data = f.read()
    
    data = data.replace("Java", "Python")
    print(data)



    

    

    