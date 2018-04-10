'''
program to recursively and non-recursively check to see if a word is a recursive_palindrome
Nate Weeks
'''

# input a string output the reverse of the string
def reverse_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse_string(string[:-1])

print reverse_string("hello World")

# input a string - output whether or not its a palindrome
def palindrome(string):
    if reverse_string(string) == string:
        return "this is a palindrome"
    else:
        return "this is not a palindrome"

print palindrome("kayak")
print palindrome("kayaks")

# input a string - output whether or not its a palindrome... recursively!
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
