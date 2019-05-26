x  = [] #Set a blank list
for i in range(2000,3201):  #set the range 2000 to 3000
    if (i%7)==0:    #divided by 7
        j = i
        if (j%5)!=0:    #not divided by 5
            x.append((j))   #add value to the list
print(x) #Printing the result from list x

