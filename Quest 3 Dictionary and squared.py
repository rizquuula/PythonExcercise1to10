x=int(input("Masukkan angka: ")) #Masukkan angka
data={} #Dictionary hasil
for i in range(x):  #Loop dengan indeks i
    j = i+1         #Supaya tidak dimulai dari nol
    data[j]=j**2    #Menghitung pangkat 2 dengan menambah key dan value ke dictionary
print(data)         #Print hasil dictionary
