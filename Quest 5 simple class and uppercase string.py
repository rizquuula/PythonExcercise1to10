class Main:             #Creating class Main
    def __init__(self,x1,x2):
        self.first = x1
        self.second = x2
name = input("Input jeneng-mu: ")
date = input("Kapan situ lahir: ")
inputed = Main(name,date)
print("jenengku " + inputed.first.upper() + " kelahiran " + inputed.second) #Uppercase all string in self.first