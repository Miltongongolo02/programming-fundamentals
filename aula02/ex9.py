def main():
    # nota final = 30% * CTP + 70% * CP
    ctp = float(input('Digite a sua nota da componente teorica-pratica (CTP): '))
    cp = float(input('Digite a sua nota da componente pratica (CP): '))

    if ctp < 6.5 or cp < 6.5:
        print('ERROR: codigo 66') # reprovado por Nota Minima.

    notaFinal = 0.3 * ctp + 0.7 * cp
    if notaFinal >= 10:
        round(notaFinal)
        print(f'O aluno aprovou com a nota: {notaFinal}')
        exit()
    
    print('Vai a recurso!')
    aptr = float(input('Digite a sua nota da componente teorica-pratica do recurso (ATPR): '))
    apr = float(input('Digite a sua nota da componente pratica do recurso (APR): '))

    notaRecurso = 0.3 * max(ctp,aptr) + 0.7 * max(cp, apr)
    round(notaRecurso)
    if notaRecurso >= 10:
        print(f'O aluno aprovou com a nota: {notaRecurso}')
    else:
        print(f'o aluno reprovou com a nota: {notaRecurso}')

if __name__ == '__main__':
    main()