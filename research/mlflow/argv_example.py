import sys
args=sys.argv
for i in args:
    print(i)

# output
"""
(/config/workspace/env) abc@d65bba49a946:~/workspace$ python research/mlflow/example.py 1,2,3,4
research/mlflow/example.py
(/config/workspace/env) abc@d65bba49a946:~/workspace$ python research/mlflow/example.py 1,2,3,4
research/mlflow/example.py
1,2,3,4
(/config/workspace/env) abc@d65bba49a946:~/workspace$ python research/mlflow/example.py 1 2 3 4
research/mlflow/example.py
1
2
3
4
"""

# Explanation

#This argv will help to pass the command line argument and store it in the form of list 
# The first element of the list is the name of python file itself 

