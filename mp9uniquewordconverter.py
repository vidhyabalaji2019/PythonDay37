# Unique Word Counter from a Paragraph

# Step 1: Ask user for input paragraph
paragraph = input("Enter a paragraph: ")

# Step 2: Convert paragraph to lowercase and split into words
words = paragraph.lower().split()

# Step 3: Store unique words in a set
unique_words = set(words)

# Step 4: Frozen set of common words to exclude
common_words = frozenset({"is", "a", "the", "and", "to", "of", "in"})

# Step 5: Remove common words from unique_words set
filtered_words = unique_words.difference(common_words)

# Step 6: Display results
print(f"\nTotal unique words (excluding common words): {len(filtered_words)}")
print("Unique words:")
for word in filtered_words:
    print(f"- {word}")
