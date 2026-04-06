""" def count_vowels(text):
    for x in text:
        if x in "aeiou":
            print(x.text.lower())
    return text
print(text("geoin")) """
def count_vowels(text):
    text = text.lower()
    total = 0
    for x in text:
        if x in "aeiou":
            total = total + 1
    return total

print(count_vowels("geoin"))
print(count_vowels("APPLE"))