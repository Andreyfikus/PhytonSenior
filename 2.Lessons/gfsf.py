from http.server import ThreadingHTTPServer


print("Hello world")

first = 23
print(first)


second = "Number" 
print(second)



print(first,second)



a = 10 + 5 
b = a + 20
c = (a + b) * 2
print(a,b,c)







first_string = "Hello world"
second_string = 'Hello world'
Third_string = """Hello world"""

name = input('Ваше імя')

greeting = "Привіт, " + name 

print(greeting)

string = input('Напишіть любий текст: ')

string_length = len(string)

print(string_length)

result = 10 + 15
text = "Результат = " + str(result)
print(text)

result_2 = "10" + "15"
text_2 = "Результат = " + result_2
print(text_2)

a_2 = input("Перше число: ")
b_2 = input("Друге число: ")

result_3 = int(a_2) + int(b_2)

text_3 = "4) Результат = " + str(result_3)
print(text_3) 

first_number = input("Перше число")
if int(first_number) == 0:
    print("Ділення на 0 не можливе.")
else:
        print("Ділення можливе.")
