def eventhenOdd(word):
    even = ''
    odd = ''
    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]

    return even + odd

def main():
    count = 0  
    while count < 3:
        word = input('Enter word: ')
        print(eventhenOdd(word))
        count += 1

if __name__ == '__main__':
    main()