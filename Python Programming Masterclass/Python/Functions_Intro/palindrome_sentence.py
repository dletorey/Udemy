def palindrome_sentence(string):
    characterless = ""
    for i in string:
        if i.isalnum():
            characterless += str(i)
    return characterless[::-1].casefold() == characterless.casefold()




sentence = input("Please enter a sentence to check if it's a palindrome")

if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))