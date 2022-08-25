rows=5
k = 64
for i in range(rows+1):
    for j in range(1,i+1):
        print(chr(k),end="")
    k += 1
    print("\r")
    
    
"""

A
BB
CCC
DDDD
EEEEE
"""
