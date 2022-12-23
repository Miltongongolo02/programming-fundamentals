def ispalindrome(word):
    word1 = ""
    for i in range(len(word)-1, -1, -1):
        word1 += word[i]

    if word1 == word:
        return True
    else:
        return False

def main():
    #testing function
     count = 0
     while count < 3:
        word = input("Enter a word: ")
        if ispalindrome(word):
            print("The word is a palindrome") 
        else:
            print("The word is not a palindrome")
        count += 1
    
if __name__ == "__main__":
    main()