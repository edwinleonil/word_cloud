# write a script to generate a world cloud using the wordcloud library
# the script should take a the column named "Public Description" from the data.csv file
# and generate a word cloud from the text in that column

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

# read the data
data = pd.read_csv("data.csv")

# get the text from the "Public Description" column and concatenate it into a single string
text = " ".join(data["Public Description"].dropna().astype(str))

# remove stop words from the text
stopwords = set(STOPWORDS)
text = " ".join([word for word in text.split()
                if word.lower() not in stopwords])

# list of words to include in the word cloud
words_to_include = ["develop", "project", "uk", "material", "iot", "device"]

# create a dictionary with frequencies for words in words_to_include
word_frequencies = {}
text_lower = text.lower()  # Convert to lowercase for case-insensitive matching
for word in words_to_include:
    word_lower = word.lower()
    # Count occurrences of the word in the text
    count = text_lower.count(f" {word_lower} ") + text_lower.count(f" {word_lower}.") + \
        text_lower.count(f" {word_lower},") + \
        text_lower.count(f"{word_lower} ")
    word_frequencies[word] = max(count, 1)  # Ensure at least frequency of 1

# plot the count of each word
plt.figure(figsize=(10, 6))
plt.bar(word_frequencies.keys(), word_frequencies.values(), color='skyblue')
plt.xlabel('Words')
plt.ylabel('Count')
plt.title('Count of Each Word in Public Descriptions')
plt.show()
