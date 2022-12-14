def main():
    segundos = int(input('Digite os segundos que demorou a chamada: '))
    ligaMin = 0.12
    assert segundos > 0
    if segundos <= 60:
        preço = ligaMin
    else:
        preco = (segundos / 60) * ligaMin
    
    print(f'O tarifário da chamada é {preco}')    

if __name__ == '__main__':
    main()