# Training a Tokenizer with Byte-Pair Encoding (BPE) for Hindi Language.

This repository contains the code for training a tokenizer with Byte-Pair Encoding (BPE) for the Hindi language. The tokenizer is trained on a dataset of Hindi text and is used to convert the text into a sequence of tokens.

## Dataset 
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/nishantbhansali/new-testament-readings-in-hindi-260-chapters)

This dataset contains 
- Chapter wise audio recordings of the New Testament (260 chapters). Files in .mp3 format. Language is Hindi
- Their corresponding transcripts in Hindi Language.

This data was scraped from the website www.faithcomesbyhearing.com
This dataset was uploaded to Kaggle for easy viewing and for the community to use.

I downloaded the audio files manually and used a script to extract the text for each of the audio recordings. I used [this file](https://github.com/nishantb06/sarvam/blob/main/part2/scraping_final.ipynb) to scrape the text off of the website and clean  up the text, (removing trailing whitespaces, removing unnecessary line breaks and numbers etc.). The final cleaned text is present in the kaggle dataset as well. 

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