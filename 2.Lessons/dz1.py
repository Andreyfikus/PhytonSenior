a = int(input('Перше число: '))
b = int(input('Друге число: '))

x = input('Знак: ')

if x == "+" :
  print(a+b)
elif x =="-" :
  print(a-b)
elif x =="*" :
  print(a*b)
elif x =="**" :
  print(a**b)
elif x =="pow" :
  print(a**b)
elif x =="" :
  print(a**b)
elif x =="/":
  if b:
    print(a/b)
  else:
    print("Ділення на 0 не можливе")