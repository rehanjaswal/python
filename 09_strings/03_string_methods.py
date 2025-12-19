x = " hello world "
print(len(x))
print(x.upper(),x)
print(x.lower())
print(x.capitalize())
print(x.title())
print(x.strip())
print(x.lstrip())
print(x.rstrip())


sentence = "CR7 is the goat"
print(sentence.replace("goat","greatest"))
print(sentence.find("goat"))


text = "MessixRonaldoxNeymar"
print(text.split("x"))        # text.split(separator) python reads from left to right and cuts the separator, removes it like a scissor, and returns a list
print("x".join(['Messi', 'Ronaldo', 'Neymar']))


x = "rehan07"
print(x.isalpha())
print(x.isnumeric())
print(x.isalnum())
print(x.isspace())   #isspace tells if a string has only whitespace characters
