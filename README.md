# cmu_2022capstone_Arboretica
This repo is for a NLP team capstone project by CMU students and Arboretica  

Note that:
1. Nearly 10 websites are protected from web scraping or don't exist. For these websites/urls, the recognized entities are empty;
2. In the training data, some urls are combines together, such as "https://www.taiwannews.com.tw/en/news/3999523; https://www.taiwannews.com.tw/en/news/3999523;...". I split them to scrape the data.
3. The ideal of recognizing the company entities is to firstly find all distinct urls, then use NLP to perform entity recognition. Then for each row in the training data, compare the entities found in corresponding urls and check whether these entities contain Company A and B. True Positive Rate is used to evaluate the algorithm performance. The TPR is 61.5%
4. Something we could consider further: (1) The TPR is not that high. (2) There are many invalid entites were recognized.
