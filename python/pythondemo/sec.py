def myfunction ():
    a=1+2
    print(a)
    if a==4:
        print("a is 2")
        x="Enter  a value X:"
        for x1 in x:
            print (x1)
        x =x.split(" ")  
        for x2 in x:
            print(x2) 
    elif a<5:   
        print("a is lessthan")     
    y= input("Enter Value ").split(" ")
    print(y)        
myfunction()
 
