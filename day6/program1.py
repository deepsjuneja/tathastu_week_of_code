def palindrome(word, i, j):
    
    if i >= j:
        return 0
    
    if word[i] == word[j]:
        return palindrome(word, i+1, j-1)
    
    return 1 + min(palindrome(word, i, j-1), palindrome(word, i+1, j))


string = input("Enter the string: ")
l = len(string)

res = palindrome(string, 0, l-1)

print("Minimum no. of deletions: ", int(res - 1))
