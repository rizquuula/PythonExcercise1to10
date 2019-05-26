x=(input('Masukkan angka: '))   #console input
y = x.split(',') #Split string 
#x = 12,34,45,6,5   #input in program
data = []           #making list
for i in (y):       #Versi manual input
    data.append(int(i))


#for i in range (len(x)):   #Versi input dalam
    #j = str(x[i])
    #data.append(j)

print (tuple(data))     #making tuple
print (data)