"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from minbpe import BasicTokenizer, RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open("tests/ONLY_New_Testament_Hindi.txt", "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("modelsV3-regex-new-testament-only", exist_ok=True)

t0 = time.time()
for TokenizerClass, name in zip([RegexTokenizer], ["regex"]):

    # construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    tokenizer.train(text, 5000, verbose=True)
    # writes two files in the models directory: name.model, and name.vocab
    prefix = os.path.join("modelsV2", name)
    tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")
