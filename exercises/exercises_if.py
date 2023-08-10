#Exercise 1 - Calculator (if/elif/else)

validate = input('Choose your language: (English/Portuguese) or (en/pt) --> ')

if validate == 'English' or validate == 'en':
    name = input('Hello, welcome to my program! To start, type your name: ')  
    print('Hello ', name,'! We will make a simple calculation for you.')
    n1 = int(input('Please, type a number: '))
    n2 = int(input('Please, type another number: '))
    calc = input('What do you want to do? (Addition/Subtraction/Multiplication/Division) You can also type the first letter of the operation you want to do. ex: (+, -, *, /): ')
    if calc == 'Addition' or calc == '+':
        print('The result is: ', n1 + n2)
    elif calc == 'Subtraction' or calc == '-':
        print('The result is: ', n1 - n2)
    elif calc == 'Multiplication' or calc == '*':
        print('The result is: ', n1 * n2)
    elif calc == 'Division' or calc == '/':
        print('The result is: ', n1 / n2)

elif validate == 'Portuguese' or validate == 'pt':
    name = input('Olá! Seja bem vindo(a) ao meu programa! Para começarmos, qual o seu nome? ')  
    print('Muito bem ', name,'! O meu sistema irá fazer um cálculo simples para você. Então siga os passos abaixo.')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    calc = input('O que você pretende fazer? (Somar, Subtrair, Multiplicar, Dividir) Você também pode teclar apenas o símbolo. ex: (+, -, *, /): ')
    if calc == 'Somar' or calc == '+':
        print('The result is: ', n1 + n2)
    elif calc == 'Subtrair' or calc == '-':
        print('The result is: ', n1 - n2)
    elif calc == 'Multiplicar' or calc == '*':
        print('The result is: ', n1 * n2)
    elif calc == 'Dividir' or calc == '/':
        print('The result is: ', n1 / n2)