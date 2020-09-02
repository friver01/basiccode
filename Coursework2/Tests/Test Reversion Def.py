def duplicatereverse(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + duplicatereverse(text[0:-1]) + text[-1]

def main():
    word = input ('Introduce text to duplicate and reverse: ', )

    print("Input  is: ", word)

    print("Duplicated and Reversed text is: ", duplicatereverse(word))

main()
