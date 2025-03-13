# write a script to generate a world cloud using the wordcloud library
# the script should take a the column named "Public Description" from the data.csv file
# and generate a word cloud from the text in that column

import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# download the stopwords from nltk
nltk.download('stopwords')

# read the data
data = pd.read_csv("data.csv")

# get the text from the "Public Description" column and concatenate it into a single string
text = " ".join(data["Public Description"].dropna().astype(str))

# convert text to lowercase and use regex to find all words
words = re.findall(r'\b\w+\b', text.lower())

# remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# count the occurrences of each word
word_counts = Counter(filtered_words)

# print the list of unique words with their corresponding count (only those with count > 50)
for word, count in word_counts.items():
    if count > 50:
        print(f"{word}: {count}")
