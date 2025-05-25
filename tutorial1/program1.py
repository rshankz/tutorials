import string


def remove_punctuation(text):
  for punctuation in string.punctuation:
    text = text.replace(punctuation, '')
  return text


printed = False
words = remove_punctuation(input("Enter a short story: ")).split()
word_counts = {}
for w in words:
  word_counts[w.lower()] = word_counts.get(w, 0) + 1
for w in words:
  if word_counts[w.lower()] > 1:
    print(f"{w} - {word_counts[w.lower()]}")
    printed = True
    word_counts[w.lower()] = 0
