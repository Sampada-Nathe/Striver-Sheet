rows=5
for i in range(rows+1):
    k = 64
    for j in range(1,i+1):
        k+=1
        print(chr(k),end="")
    print("\r")
    
    
"""
A
AB
ABC
ABCD
ABCDE
"""
