#Números Primos

num = int(input('\033[0mDigite um número inteiro: \033[m'))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[1;32m{i}\033[m')
        tot += 1
    else:
        print(f'\033[1;31m{i}\033[m')

if tot == 2:
    print('\033[4;34mEsse número é primo!\033[m')
else:
    print('\033[4;34mEsse número não é primo!\033[m')

print(f'\033[0;33mO número {num} foi divisível por {tot} vezes.\033[m')
