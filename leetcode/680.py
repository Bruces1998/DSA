'''
https://leetcode.com/problems/valid-palindrome-ii/
'''

def isPallindrome(string):
    start = 0
    end = len(string)-1

    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True

def validPallindrome(string):
    
    start = 0
    end = len(string)-1

    while start < end and string[start] == string[end]:
        start += 1
        end -= 1

    return isPallindrome(string[i+1, j+1]) or isPallindrome(string[i:j])

    