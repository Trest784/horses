n=int(input("Enter the number:\n")) # Alexey
                                 # в инпутах лучше делать пробел в конце или же
                                 # даже '\n' чтобы отделять вводимые данны и 
                                 # интерфейс
factorial = 1
for i in range(2,n+1):
    fact=factorial * i
print('Factorial =',fact)


n=9 # Alexey: зачем тогда в строке один ты получаешь n если здесь его меняешь на 
    # 9, лучше уже работать с вводными чтобы видеть динамику
fact=1
for i in range(2,n+1):
    fact=fact*i # Alexey: эквивалентно более популярной и лаконичной записи 
#   fact *= i
print("The factorial of",n,"is:",fact)

n = 3 # Alexey: ну то же что и в 10 строке
fact = 1
for i in range(4):
    factorial = fact * i
    print(factorial)





