def reverse_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse_string(string[:-1])

print reverse_string("hello World")

def palindrome(string):
    if reverse_string(string) == string:
        return "this is a palindrome"
    else:
        return "this is not a palindrome"

print palindrome("kayak")
print palindrome("kayaks")

def recursive_palindrome(string):
    if len(string) == 1:
        return "yay it's a palindrome!"
    else:
        if string[-1] == string[0]:
            return recursive_palindrome(string[1:-1])
        else:
            return "not a palindrome"

print recursive_palindrome("aibohphobia")
print recursive_palindrome("kayaks")
