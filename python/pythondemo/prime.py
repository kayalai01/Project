for num in range(2, 25):        # 2,3,4,5,
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):  # 2 
           if (num % i) == 0:
               break
       else:
           print(num)
        