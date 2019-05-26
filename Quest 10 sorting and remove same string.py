#Sorted input and eliminate same string
kalimat = input("Masukkan kalimat: ").split(" ")
kalimat.sort()  #Sorting input
hasil = list(dict.fromkeys(kalimat))    #Remove same string in list
print(kalimat) 
print(hasil)