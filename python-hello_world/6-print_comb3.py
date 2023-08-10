#!/usr/bin/python3
def comb(L):  
    a=int(input("Enter first number:"))  
    b=int(input("Enter second number:"))  
     
    L.append(a)  
    L.append(b)   
    for j in range(2):  
        for k in range(2):       
            # check if the indexes are not  
            # same  
            if (j!=k or j == k): 
                print(L[k], L[j])
comb([])
