def is_palindrome(text):
    clean_input = ''
    for char in text:
        if char.isalnum():
            clean_input += char.lower()
    reverse_text = clean_input[::-1]
    return clean_input == reverse_text


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
