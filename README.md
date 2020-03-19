# decryptor
Computer player for the card game "Decrypto".

https://www.scorpionmasque.com/en/decrypto

### Dependencies
Works with Python >3.6. You need gensim to be installed.

Also you need to download the models "dewiki_20180420_300d.txt" and "enwiki_20180420_300d.txt" 
from https://wikipedia2vec.github.io/wikipedia2vec/pretrained/ 

You can also use other pretrained models, they just need to be in the word2vec text format. Then you also 
have to change the names of the models in the code.

### Usage
Start it without parameters to have the computer play a game of "Decrypto" with you.

You can use the following arguments:
```optional arguments:
  -h, --help      show this help message and exit
  --german, -g    Use German version (default: English)
  --example, -e   Use example Data (default: play
  --beispiel, -b  Use german example Data ( default: play)
  --fast, -f      Use smaller vocabulary for smaller memory or faster loading
                  time.
```
