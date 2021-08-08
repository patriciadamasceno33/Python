import os
import sys

def directories(path_A, path_B):
    path_A = (os.listdir('C:/Intel/Logs'))
    path_B = (os.listdir('C:/Intel/fakelogs'))
    return(path_A, path_B)

pA = pB = ''
print(len(sys.argv))
(sys.argv[1]) = pA
(sys.argv[2]) = pB
print(sys.argv[0])
print(directories(sys.argv[1], sys.argv[2]))
