# This works

#Loading NLTK
import nltk
import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import lexnlp.nlp.en.tokens
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Establish stopwords
stop_words=set(stopwords.words("english"))

# Read text file
path = 'vol-1.txt'
text=open(path, 'r')
text = text.read() # Text to string

tokenized_text=sent_tokenize(text)
# print(tokenized_text)

tokenized_word = lexnlp.nlp.en.tokens.get_token_list(text, lowercase=True, stopword=True)

# Remove stop words
# filtered_sent=[]
# for w in tokenized_text:
#     if w not in stop_words:
#         filtered_sent.append(w)
# text = filtered_sent

# tokenized_word=word_tokenize(text)
# tokenized_word=text
# print(tokenized_word)

fdist = FreqDist(tokenized_word)
# print(fdist)

fdist.most_common(2)

# Frequency Distribution Plot
fdist.plot(30,cumulative=False)
plt.show()

# Close file
# text.close() # String has no attribute close()
