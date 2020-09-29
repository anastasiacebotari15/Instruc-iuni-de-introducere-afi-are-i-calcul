""" se introduc de la tastatura trei cifre. Afisati pe aceeasi linie 5 numere formate cu 
aceste cifre luate o singura data"""
x=int(input("Introduceti 1 nr:"))
y=int(input("Introduceti 2 nr:"))
z=int(input("Introduceti 3 nr:"))
print(str(x)+str(y)+str(z), str(y)+str(z)+str(x), str(z)+str(y)+str(x), str(y)+str(x)+str(z), str(z)+str(x)+str(y), str(x)+str(z)+str(y))