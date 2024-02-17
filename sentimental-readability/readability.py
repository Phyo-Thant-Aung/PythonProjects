from cs50 import get_string

text = get_string("Text: ")

Letters = 0
for i in text:
    if (i.isalpha() == True):
        Letters += 1

Words = len(text.split()) #formula from https://blog.finxter.com/how-to-count-the-number-of-words-in-a-string-in-python/#:~:text=Approach%3A%20To%20separate%20out%20each,words%20in%20the%20given%20string.

Sentences = 0
for i in text:
    if i == '.' or i == '!' or i == '?':
        Sentences += 1

calculation = float((0.0588 * Letters / Words * 100) - (0.296 * Sentences / Words * 100) - 15.8)
index = round(calculation)

if (index < 1):
    print("Before Grade 1")
elif(index >= 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")