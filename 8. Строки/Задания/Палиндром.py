def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True

print( 'Yes' if is_palindrome("radar") else 'No')
#print(is_palindrome("radar"))