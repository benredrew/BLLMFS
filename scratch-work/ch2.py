"""
Author: Brendan Fennell
Instructor: Sebastian Raschka
Text: Building A Large Language Model From Scratch
Unit: Chapter 2
"""

import urllib.request
import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

# Open the-verdict.txt and print number of characters
with open("the-verdict.txt","r",encoding="utf-8") as f:
    raw_text=f.read()
print("Total number of character:",len(raw_text))

# Tokenize the-verdict.txt and print number of tokens
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print("Total number of tokens:",len(preprocessed))

# Create a vocabulary and print the number of entries
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
vocab = {token:integer for integer,token in enumerate(all_words)}
print("Total number of vocabulary entries:",vocab_size)

# Instantiation of a new tokenizer object, and using it
tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
print("Section of text:",text)
ids = tokenizer.encode(text)
print("ID's from the section of text:",ids)
print("Transforming ID's back to text:",tokenizer.decode(ids))