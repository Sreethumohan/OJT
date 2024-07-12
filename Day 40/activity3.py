import collections

# Long text
text = """Flowers are nature’s way of 
adding color and beauty to the world, 
each bloom a unique masterpiece that 
can brighten any day. 🌸."""

# Print the long text
print("Original Text:")
print(text)

# Convert the text to a list of words
words = text.lower().split()

# Print the list of words
print("\nList of Words:")
print(words)

# Count the frequency of each word
word_freq = collections.Counter(words)

# Print the frequency of each word
print("\nFrequency of Each Word:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")