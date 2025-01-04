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

Data after downloading will look like this:
|___data___|
    |___Hindi_hin_BCS_NT_Non-Drama___|
        |___B01___01_Matthew_____HINBCSN1DA.mp3___|
        |___B01___02_Matthew_____HINBCSN1DA.mp3___|
        |___B01___03_Matthew_____HINBCSN1DA.mp3___|
        .
        .
        .
        |___B260___01_Revelation_____HINBCSN260DA.mp3___|
        |___B260___02_Revelation_____HINBCSN260DA.mp3___|
        |___B260___03_Revelation_____HINBCSN260DA.mp3___|
        .
        .
        .
    |___Hindi_hin_BCS_NT_Non-Drama_transcripts___|
        |___B01___01_Matthew_____HINBCSN1DA.txt___|
        |___B01___02_Matthew_____HINBCSN1DA.txt___|
        |___B01___03_Matthew_____HINBCSN1DA.txt___|
        .
        .
        .
        |___B260___01_Revelation_____HINBCSN260DA.txt___|
        |___B260___02_Revelation_____HINBCSN260DA.txt___|
        |___B260___03_Revelation_____HINBCSN260DA.txt___|
        .
        .
        .   
________________________________________________________________________________________