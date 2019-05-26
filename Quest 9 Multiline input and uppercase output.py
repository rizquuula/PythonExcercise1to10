print("Masukkan kalimat anda: ") #Title
box = []
while True:
    print("> ",end="")  #No enter print
    kalimat = input()   #Input
    if kalimat=='':
        break           #Stop the loop while it is blank input
    else:
        box.append(kalimat)     #insert input to box

for i in range(len(box)):
    print(box[i].upper()) #print input in diferent line and uppercase it
