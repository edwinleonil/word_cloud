# write a script to generate a world cloud using the wordcloud library
# the script should take a the column named "Public Description" from the data.csv file
# and generate a word cloud from the text in that column

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# read the data
data = pd.read_csv("data.csv")

# get the text from the "Public Description" column and concatenate it into a single string
text = " ".join(data["Public Description"].dropna().astype(str))

# list of words to include in the word cloud
words_to_include = ["metaverse", "netzero", "blockchain", "cryptographic", "iot",
                    "aerostructures", "musculoskeletal", "hyperspectral", "haptic", "hospitality"]

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

# create a word cloud from the word frequencies
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=None,
                      min_font_size=10).generate_from_frequencies(word_frequencies)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
