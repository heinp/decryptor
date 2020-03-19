# decryptor
Computer player for the card game "Decrypto".

https://www.scorpionmasque.com/en/decrypto


### Idea
There are two rules regarding the clues:

> **The Clues must refer to the meaning of the Keywords.**
>
> The Clues must never refer to the spelling (“C” to hint at “Cursed”), the number of letters (“8” or “8 letters” to hint at “Scorpion”), the position on the Screen (“musketeers” to hint at the word in the third position), or pronunciation (“face” to make your team guess “Place”).
>
> **The Clues must be based on information that is publicly available.**
>
> You can certainly refer to obscure Croatian poets of the 17th Century—it’s risky, but allowed! However, you may NEVER refer to “private” items, like what you ate for lunch or little sweet nothings between you and your spouse.


This allows an approach based on distributional semantics, approximating word similarity (as in means something similar) and word closeness (as in belongs to the same semantic theme) using cosine similarity in a vector space model. Handling references to Croatian poets of the 17th Century is not possible yet, but might be implemented in the future (maybe parsing Wikipedia articles or the first 10 Google hits).


### Dependencies
Works with Python >3.6. You need gensim to be installed.

Also you need to download the models "dewiki_20180420_300d.txt" and "enwiki_20180420_300d.txt" 
from https://wikipedia2vec.github.io/wikipedia2vec/pretrained/. Store them in a folder called "models" in the decryptor folder.

You can also use other pretrained models, they just need to be in the word2vec text format. 

### Usage
Start it without parameters to have the computer play a game of "Decrypto" with you.

You can use the following arguments:
```  --german, -g          use German version
  --example, -e         use example Data
  --beispiel, -b        use german example Data
  --fast, -f            use smaller vocabulary for smaller memory or faster
                        loading time
  --model MODEL, -m MODEL
                        path to model, if not default

```
