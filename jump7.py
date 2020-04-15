for num in (1,101):
    if num % 7 == 0:
        continue
    elif num % 10 == 7:
        continue
    elif num // 7 == 0:
        continue
    else :
        print(num)
     
