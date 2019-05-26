import numpy as np      #Import numpy and call it np
C = 50      #fix number
H = 30      #fix number
Q = []
inputD = (input("Masukkan beberapa angka dipisahkan dengan koma: "))    #input number
splitD = inputD.split(",")      #making list from string
for i in range(len(splitD)):
    D = int(splitD[i])          #convert string list to integer
    Q.append(int(np.sqrt((2*C*D)/H)))   #formula to empty list Q

print(Q)    #Printing list of result
