a = input("Перше число: ")
b = input("Друге число: ")

c = input("Виберіть дію")

if c == '+':
    print('a + b = ' , str(int(a) + int(b)))
elif c == '-':
    print('a - b = ' , str(int(a) - int(b)))
elif c == '*':
    print('a * b = ' , str(int(a) * int(b)))
elif c == '/':
    if b == '0':
        print("ERROR")
    else:
     print('a / b = ' , str(int(a) / int(b)))


    
