# cmu_2022capstone_Arboretica
This repo is for a NLP team capstone project by CMU students and Arboretica  

Our project goal is to develop an algorithm solution for our client, Arboretica, to extract financial relationships from texts more dynamically. To complete this project, we conducted literature research, explored different natural language processing techniques, expanded our dataset, and fine-tuned an advanced algorithm tailored to our client’s needs. Our algorithm is expected to significantly reduce human efforts.

## Repo Content Overview

### Step 1: Data
- `scraping.ipynb` 

This is the code for data_scraping. There are two sections for scraping tech and financial news. The packages used are BeautifulSoup and newspaper3k.

- `Data cleaning and preprocessing.ipynb`
...

- `train_data_arboretica.csv`


The original data provided by Arboretica. 

- `Cleaned_full_data.csv`
...

### Step 2: NER + LUKE
- `Spacy-NER(Roberta).ipynb`


Our baseline model using spaCy. 

- `Luke_NER.ipynb`

- `Luke_NER_full_data.ipynb`

- `Multi_label_relationship_extraction.ipynb`

- `Annotated_Multi_label_relationship_extraction.ipynb`



