def multiply(x: float, y: float) -> float:
    """
    Takes 2 numbers `x` and `y` and returns that value when multiplied
    :param x: first number to be multiplied
    :param y: number to be multiplied by x
    :return: value of x times y
    """
    result = x * y
    return result

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# tests
word = input("please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# Using Multiply function
# answer = multiply(64736, 5)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print("-" * 10)
#
# for val in range (1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
#
