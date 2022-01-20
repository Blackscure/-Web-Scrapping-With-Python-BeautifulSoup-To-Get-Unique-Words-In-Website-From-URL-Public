import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')


res = requests.get('https://stackoverflow.com/')

# Parsing web content acquired as html
soup = BeautifulSoup(res.content, 'html.parser')

# Removing html tags from response soup
good = ''.join(soup.stripped_strings)

# print(good)
# print(type(good))

# Defining punctuation list
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''

# Removing all punctuations from variable good value of all text and setting unpunctuated string to no_punc variable
no_punc = ""
for char in good:
    if char not in punctuations:
        no_punc = no_punc + char

# print(no_punc)
# print(type(no_punc))

# Splitting non punctuated result to get every individual word without punctuations
splitted = no_punc.split()
# print(splitted)
# print(type(splitted))

# getting all unique words from split result in splitted variable and appending all unique words to variable unique_words
unique_words = []
for i in splitted:
    if not i in unique_words:
        unique_words.append(i)
print(unique_words)


status = res.status_code
print(status)


if __name__ == '__main__':
    print('Python')
