graus_Fahren = input('Insira o valor em graus fahrenheit para convertê-lo em celsius: ')

graus_Fahren_int = eval(graus_Fahren)
print('Você digitou ', graus_Fahren_int)
celsius = (graus_Fahren_int - 32)*5/9

print('O valor em graus é:', celsius)