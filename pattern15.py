rows=5
for i in range(rows+1):
    k = 64
    for j in range(rows-i,0,-1):
        k+=1
        print(chr(k),end="")
    print("\r")

    
"""
ABCDE
ABCD
ABC
AB
A
"""
