def calc(x,y,ops):

    if ops not in "+*/-":
        return("You entry a invalid command.")
    
    if ops == "+":
        return(str(x) + " " + ops + " " + str(y) + "=" + str(x+y))
    
    elif ops == "-":
        return(str(x) + " " + ops + " " + str(y) + "=" + str(x-y))
    
    elif ops == "*":
        return(str(x) + " " + ops + " " + str(y) + "=" + str(x*y))
    
    elif ops == "/":
        return(str(x) + " " + ops + " " + str(y) + "=" + str(x/y))
    
x = int(input("Please enter a first value:"))
    
y = int(input("Please enter a second value:"))

ops = input("Chooes between '+*-/'")
        
print(calc(x,y,ops))


