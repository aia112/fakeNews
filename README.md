Project Summary: Fake News Detection Using Naive Bayes

The "Fake News Detection" project involves building a machine learning model to identify and classify news articles as either "fake" or "real." The project leverages a Naive Bayes classifier, a simple yet powerful probabilistic model, well-suited for text classification tasks.

Steps Involved:

1. Data Collection:
   - News articles were scraped from various reputable and non-reputable news sources to create a balanced dataset. These sources include a mix of mainstream media, independent journalism sites, and known sources of misinformation.

2. Data Cleaning:
   - The scraped data underwent extensive preprocessing to remove noise. This included:
     - Removing HTML tags: Stripping out any remaining HTML from the scraped text.
     - Tokenization: Breaking down the text into individual words or tokens.
     - Stopword Removal: Eliminating common, uninformative words (like "the," "and," etc.) that do not contribute to the classification.
     - Lemmatization/Stemming: Reducing words to their base or root form to ensure consistency in word representation.

3. Feature Extraction:
   - After cleaning, the text data was converted into numerical features suitable for input into the Naive Bayes model. Techniques like Term Frequency-Inverse Document Frequency (TF-IDF) were employed to quantify the importance of words across the dataset.

4. Model Building:
   - A Naive Bayes classifier was selected due to its effectiveness in handling text data, especially in binary classification tasks like fake news detection.
   - The model was trained on a labeled dataset of news articles, where each article was tagged as "fake" or "real" based on its source and content.

5. Model Evaluation:
   - The performance of the model was evaluated using metrics such as accuracy, precision, recall, and F1-score. Cross-validation was employed to ensure the model’s robustness and to avoid overfitting.
   - The model's ability to correctly identify fake news articles was emphasized, with the aim of minimizing false positives and false negatives.

6. Deployment:
   - Once trained and validated, the model was packaged into a user-friendly application where users could input a link to the article , and receive an assessment of whether the article is likely to be fake or real.
