# cmu_2022capstone_Arboretica
This repo is for a NLP team capstone project by CMU students and Arboretica  

Note that:
1. Nearly 10 websites are protected from web scraping or don't exist. For these websites/urls, the recognized entities are empty.
2. In the training data, some urls are combines together, such as "https://www.taiwannews.com.tw/en/news/3999523; https://www.taiwannews.com.tw/en/news/3999523;...". I split them to scrape the data.
3. Some company names are shorter in the traning data than in the original article, for example, 'fortino capital' in training data vs 'fortino capital partners' in the article.
4. The steps of recognizing the company entities are: firstly find all distinct urls, then use NLP to perform entity recognition. For each row in the training data, identify the entities recognized in corresponding urls and check whether these entities contain Company A and B. True Positive Rate is used to evaluate the algorithm performance. The TPR is 61.5%
5. Something we could consider further: (1) The TPR is not that high. (2) There are many invalid entites recognized.
