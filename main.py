#Função para verificar se o número é primo
def is_prime(number):
    if number == 2 or number == 3: return True
    if number%2 == 0 or number < 2: return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number%i == 0:
            return False
    return True

#Código Principal
euler_text = open('eNumber.txt').read().replace('.', '')
for i in range(len(euler_text)):
    if is_prime(int(euler_text[i:i+10])):
        print(f'The result is {euler_text[i:i+10]}.com')
        break