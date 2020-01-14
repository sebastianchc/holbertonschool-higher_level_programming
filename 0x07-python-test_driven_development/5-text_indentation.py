#!/usr/bin/python3
def text_indentation(text):
    position = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        while position < len(text):
            print(text[position], end="")
            if text[position] in [".", "?", ":"]:
                print("\n")
                if text[position + 1] == " ":
                    position += 1
            position += 1
