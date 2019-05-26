#Program untuk menghitung faktorial
 
x=int(input("Masukkan angka: "))    #Input angka secara konsol
y=[]    #Kotak angka secara urutan 1,2,3,4, dst..
z=1     #Bagian yang akan jadi patokan saat loop hitung
for i in range(x):  
    y.append(i+1)   #Kalau tidak di +1 hasilnya akan 0
for j in range(len(y)):
    z=z*y[j]        #Loop hitungan sehingga semua dikalikan
print(z)      #Hasil akhir setelah loop berhenti
    
