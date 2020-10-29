def is_palindrome(string):
    """
    Takes a string to see if it a palindrome,
        the same forward as backward
    :param string: String that is to be checked as a palindrome.
    :return: True is the `string` is the same backward as forwads
        otherwise False
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    """
    Takes a `String` and checks each character to see if it is a number or letter,
        and if it is adds it to a new string called characterless.
        Then uses that string in the `is_palindrome` function
    :param string: The sting of characters that will have any non alpha numeric characters removed
    :return: True if the `characterless` string is a palindrome, otherwise
        False
    """
    characterless = ""
    for i in string:
        if i.isalnum():
            characterless += str(i)
    # return characterless[::-1].casefold() == characterless.casefold()
    return is_palindrome(characterless)




sentence = input("Please enter a sentence to check if it's a palindrome")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))