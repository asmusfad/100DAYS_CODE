def text_processor(text):
  
  words = text.split()
  unique_words = set(words)
  words_length = [len(word) for word in words]
  
  max_length = max(words_length) if words_length else 0
  longest_words = [word for word in unique_words if len(word) == max_length]
  print()
  return longest_words, len(unique_words)

#Example
print(text_processor("Hello world hello Python"))