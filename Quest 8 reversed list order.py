text = input("Masukkan kata dipisahkan koma: ").split(',') #Split input to list
box = []    #Blank list 
for i in range(len(text)):
    if i==(len(text)-1):
        box.append(text[i])     #Last list that pushed into the box
    else:
        box.append(text[len(text)-i-2]) #Push reverse list order
print(box)  #Print list
'''
EXAMPLE:
INPUT:  aku,kamu,dia,siapa,yaa,haha,apa,sih,kok,gaje
OUTPUT: ['kok', 'sih', 'apa', 'haha', 'yaa', 'siapa', 'dia', 'kamu', 'aku', 'gaje']
'''