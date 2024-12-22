import os


def sortLength():
    file=open("day1Input.txt","r")
    arr=[]
    arr1=[]
    arr2=[]
    temp1=""
    for line in file.readlines():
       arr1.append(int(line[:5]))
       arr2.append(int(line[8:13]))
    
    print(temp1[:5])
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    result=0
    for i in range(0,len(arr1)):
        result+=abs(arr1[i]-arr2[i])
    print(result)

    #Part 2
    score=0
    multiplier=0
    for i in range(0,len(arr1)):
        multiplier=0
        for j in range(0,len(arr1)):
            if(arr1[i]==arr2[j]):
                multiplier+=1
        score+=arr1[i]*multiplier
    print(score)
sortLength()