from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Load the Excel file
df = pd.read_excel('/Users/mengyuefan/Downloads/responses.xlsx', sheet_name='20171-Fan-2232')

# The text is in a column named 'Text'
text_data = df['Text'].str.cat(sep=' ')  # Concatenate all text into one string, separated by spaces

# Define custom stopwords
custom_stopwords = set(STOPWORDS)
additional_stopwords = {'Mengyue', 'Fan', 'class', 'professor', 'teacher', 'teaching', 'lecture', 'content', 'instructor', 'students', 'assignment', 'material' }
custom_stopwords.update(additional_stopwords)

# Create a word cloud object with these stopwords
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=custom_stopwords).generate(text_data)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Save the word cloud to a file
wordcloud.to_file('Eval.png')
