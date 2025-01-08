# Training a Tokenizer with Byte-Pair Encoding (BPE) for Hindi Language.

Hugging Face Spaces: https://huggingface.co/spaces/nishantb06/hindi-tokenizer-bpe-v2


This repository contains the code for training a tokenizer with Byte-Pair Encoding (BPE) for the Hindi language. The tokenizer is trained on a dataset of Hindi text and is used to convert the text into a sequence of tokens.

### Final compression ratio: 10.18X

### Vocab size: 5000


## Regex pattern used:
`HINDI_SPLIT_PATTERN_V2 = r'\s*(?:[\u0900-\u097F\u0981-\u0983]+|\d+|[^\s\w\u0900-\u097F\u0981-\u0983])'`

Why is the regex pattern used?
When working with languages other than English, it is important to use the regex pattern to ensure that bytes belonging to the same token are not split, thus creating a lot of unknown tokens. 
Therefore it becomes important to ensure that the words are first split by space and that the verbs of Hindi lanuage are not split. Taking care of numbers and other special characters is also important. 

### logs
```
compression ratio: 10.18X
merge 4691/4744: (4945, 260) -> 4946 (b' \xe0\xa4\x97\xe0\xa4\xa1\xe0\xa5\x8d\xe0\xa4\xa2\xe0\xa5\x87') had 4 occurrences
compression ratio: 10.18X
merge 4696/4744: (320, 610) -> 4951 (b'\xe0\xa4\xaa\xe0\xa5\x81\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0') had 4 occurrences
compression ratio: 10.18X
merge 4701/4744: (1351, 291) -> 4956 (b'\n\xe0\xa4\xb9\xe0\xa4\xae\xe0\xa4\xa8\xe0\xa5\x87') had 4 occurrences
compression ratio: 10.18X
merge 4706/4744: (3077, 445) -> 4961 (b' \xe0\xa4\xa8\xe0\xa4\xbf\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xac\xe0\xa5\x81\xe0\xa4\xa6\xe0\xa5\x8d\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\xaf\xe0\xa5\x8b\xe0\xa4\x82') had 4 occurrences
compression ratio: 10.18X
merge 4711/4744: (4965, 2081) -> 4966 (b' \xe0\xa4\xb8\xe0\xa5\x83\xe0\xa4\x9c\xe0\xa4\xa8\xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb0') had 4 occurrences
compression ratio: 10.18X
merge 4716/4744: (278, 298) -> 4971 (b' \xe0\xa4\xb8\xe0\xa4\xbe\xe0\xa4\xb0') had 4 occurrences
compression ratio: 10.19X
merge 4721/4744: (4975, 2672) -> 4976 (b' \xe0\xa4\xaa\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xa4\xe0\xa4\xbf\xe0\xa4\xb5\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xb7') had 4 occurrences
compression ratio: 10.19X
merge 4726/4744: (10, 822) -> 4981 (b'\n\xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\x81') had 4 occurrences
compression ratio: 10.19X
merge 4731/4744: (1639, 260) -> 4986 (b' \xe0\xa4\x85\xe0\xa4\x9a\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xad\xe0\xa5\x87') had 4 occurrences
compression ratio: 10.19X
merge 4736/4744: (364, 1150) -> 4991 (b'\xe0\xa4\xbe\xe0\xa4\xb2\xe0\xa5\x80\xe0\xa4\xb8') had 4 occurrences
compression ratio: 10.19X
merge 4741/4744: (4995, 645) -> 4996 (b' \xe0\xa4\x96\xe0\xa4\xbf\xe0\xa4\xa1\xe0\xa4\xbc\xe0\xa4\x95\xe0\xa5\x80') had 4 occurrences
compression ratio: 10.19X
Training took 6005.98 seconds
```



## Dataset

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/nishantbhansali/new-testament-readings-in-hindi-260-chapters)

This dataset contains

- Chapter wise audio recordings of the New Testament (260 chapters). Files in .mp3 format. Language is Hindi
- Their corresponding transcripts in Hindi Language.

This data was scraped from the website www.faithcomesbyhearing.com
This dataset was uploaded to Kaggle for easy viewing and for the community to use.

I downloaded the audio files manually and used a script to extract the text for each of the audio recordings. I used [this file](https://github.com/nishantb06/sarvam/blob/main/part2/scraping_final.ipynb) to scrape the text off of the website and clean up the text, (removing trailing whitespaces, removing unnecessary line breaks and numbers etc.). The final cleaned text is present in the kaggle dataset as well.

## Dataset Structure

After downloading, the data will be organized as follows:

data/
├── Hindi_hin_BCS_NT_Non-Drama/ # Audio files directory
│ ├── B01_01_MatthewHINBCSN1DA.mp3
│ ├── B01_02_MatthewHINBCSN1DA.mp3
│ ├── B01_03_MatthewHINBCSN1DA.mp3
│ │ ...
│ ├── B260_01_RevelationHINBCSN260DA.mp3
│ ├── B260_02_RevelationHINBCSN260DA.mp3
│ └── B260_03_RevelationHINBCSN260DA.mp3
│
└── Hindi_hin_BCS_NT_Non-Drama_transcripts/ # Transcript files directory
├── B01_01_MatthewHINBCSN1DA.txt
├── B01_02_MatthewHINBCSN1DA.txt
├── B01_03_MatthewHINBCSN1DA.txt
│ ...
├── B260_01_RevelationHINBCSN260DA.txt
├── B260_02_RevelationHINBCSN260DA.txt
└── B260_03_RevelationHINBCSN260DA.txt

# resources

- [Beyond the ABCs: Exploring the nuances of tokenization in diverse languages](https://www.icodeformybhasa.com/p/beyond-the-abcs-exploring-the-nuances)
-
