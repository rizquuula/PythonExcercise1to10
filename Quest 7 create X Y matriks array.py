XY = input("Masukkan X,Y yang diinginkan: ").split(',') #Decide X is ROW and Y is COLUMN
X = int(XY[0])  #Split to X
Y = int(XY[1])  #Split to Y
GlobalArr = []  #Global array
Arr = []    #Specific array
for i in range(0,X):
    for j in range(0,Y):
        Arr.append(j*i)     #Set one group of array first
    GlobalArr.append(Arr)   #Then push it to the global
    Arr = []                #Delete the local array so it can filled again and push it again in loop
    
print(GlobalArr)    #Print the final result