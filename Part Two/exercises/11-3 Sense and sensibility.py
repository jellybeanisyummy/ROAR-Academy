import PyPDF2
import os

# get current file location
current_dir = os.path.dirname(os.path.abspath(__file__))

file_handle = open(current_dir + '/Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)
page_number = len(pdfReader.pages)   # this tells you total pages


# page_object = pdfReader.pages[0]    # We just get page 0 as example 
# page_text = page_object.extract_text()   # this is the str type of full page

distinct_words = {}

for pages in range(page_number):
    page_object = pdfReader.pages[pages]
    page_text = page_object.extract_text()   # this tells you the text of the page
    lines = page_text.split('\n')  # split the text into lines
    for line in lines:
        for char in line:
            if char.isalpha() == False and char != ' ':  # check if the character is not a letter and not a space
                line = line.replace(char, ' ')  # replace punctuation with a space

        words = line.split(" ")
        for word in words:
            chars = list(word)

            bad_word_for_dict = True
            for char in chars:       # check if we can put this word in dictionary
                if char.islower():
                    bad_word_for_dict = False
            word = ''.join(chars)  # join the characters back into a word

            if bad_word_for_dict:       # go to next word
                continue

            word = word.lower()
            if word not in distinct_words:
                distinct_words[word] = 1
            else:
                distinct_words[word] += 1

print(distinct_words)