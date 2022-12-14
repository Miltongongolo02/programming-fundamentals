def main():
    age = int(input('Digite a sua idade: '))
    if age == 0:
        print('ERROR: Invalid age value!')
        exit()

    if age < 13:
        category = 'child'
    elif age < 20:
        category = 'teenager'
    else:
        category = 'grown-up'

    print(f'category : {category}')

if __name__ == '__main__':
    main()