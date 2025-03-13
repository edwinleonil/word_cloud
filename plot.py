# write a script to generate a world cloud using the wordcloud library
# the script should take a the column named "Public Description" from the data.csv file
# and generate a word cloud from the text in that column

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# read the data
data = pd.read_csv("data.csv")

# get the text from the "Public Description" column and concatenate it into a single string
text = " ".join(data["Public Description"].dropna().astype(str))

# create a word cloud
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(text)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
