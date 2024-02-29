# Given a positive integer, write a function that returns true if the given number is a palindrome, else false.
# For example, 12321 is a palindrome, but 1451 is not a palindrome.

n = int(input("Enter a positive integer:"))


def reverse(n):
    if n < 10:
        return n
    elif n > 0:
        return int(str(n % 10) + str(reverse(n // 10)))


def palindrome(n):
    if n == reverse(n):
        return True
    else:
        return False


reverse(n)
palindrome(n)