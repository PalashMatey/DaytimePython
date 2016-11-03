def isPalindrome(s):
    valid = []
    for character in s:
        if character.isalpha():
            valid.append(character)
        else:
            continue
    word = ''.join(valid).lower()
    
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])


answer = isPalindrome("A man, a plan, a canal: Panama")
print answer