#will print the multiplication table of the given number upto 10
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
count = 1        
print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number * 1    
    print (number, 'x', count, '=', number * count)    
    count += 1    
