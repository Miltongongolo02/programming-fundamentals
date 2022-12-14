def main():
    while True:
        peso = float(input('Digite o seu peso: '))
        if peso < 0:
            print('Digite o seu peso inválido')
            continue
        else:
            break
        
    while True:
        altura = float(input('Digite a sua altura: '))
        if altura < 0:
            print('Digite a sua altura inválida')
            continue
        else:
            break

    imc = peso / (altura ** 2)

    if imc < 18.5:
        category = 'Magro'
    elif imc < 25:
        category = 'Saudável'
    elif imc < 30:
        category = 'Forte'
    else:
        category = 'Obeso'

    print(f'category: {category}')

if __name__ == '__main__':
    main()