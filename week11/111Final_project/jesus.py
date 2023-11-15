from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define the passage to visualize
text = "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."

# Create a WordCloud object with custom parameters
wordcloud = WordCloud(width=800, height=400, background_color="white", max_words=50).generate(text)

# Display the WordCloud using matplotlib
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

