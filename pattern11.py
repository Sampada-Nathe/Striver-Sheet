rows=5
for i in range(rows+1):
    for j in range(i):
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
            print(0, end=" ")
        else:print(1,end=" ")
    print("\r")

    
"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
