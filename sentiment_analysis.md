**Project name: sentiment_analysis.py**

**SUMMARY**
  
1. [Description](#1-description)
2. [Installation](#2-installation)
3. [How to Use](#3-how-to-use)
4. [Credits](#4-credits)
5. [Limitation](#5-limitation)

<a name="readme-top"></a>

## 1. Description: 

The dataset lists over 34,000 consumer reviews for Amazon products like the Kindle, Fire TV Stick, and more provided by Datafiniti's Product Database. 

The dataset includes basic product information, rating, review text, and more for each product.

Consumer Reviews of Amazon Products (Dataset link):  https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 2. Installation:

_To get a local copy up and running follow these simple steps._

1. Clone the repository:
   ```sh
   git clone https://github.com/JulianaRibr/finalCapstone.git
   ```
2. Download the csv file from kagle.com (link on the description).
3. 
4. Save the file in the same local folder where you will save the program to be run.

5. Run the code:
   ```sh
   python sentiment_analysis.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 3. How to Use:

The program starts, presenting to the user the libraries he'll use.

![Screenshot of a piece of the code.](https://github.com/JulianaRibr/finalCapstone/assets/153245025/641ac39f-e5ae-49b7-9a4a-bf7497c25876)

After that shows the functions that will promote data cleaning and review analysis.

![Screenshot of a piece of the code.](https://github.com/JulianaRibr/finalCapstone/assets/153245025/a0f1102d-86d8-437e-beab-24c29058d534)

After reading the data and running the lines of code,  you will obtain the
percentages relating to positive and negative customer feelings as output. 

![Screenshot of a piece of the code.](https://github.com/JulianaRibr/finalCapstone/assets/153245025/a0f1102d-86d8-437e-beab-24c29058d534)

Based on these scores, you can proceed with your analyse.




<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 4. Credits:
Project created by **<https://github.com/JulianaRibr>**.

Template of the README.MD based on <https://github.com/othneildrew/Best-README-Template/tree/master>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 5. Limitation

From what it could be seen, spacy analyses the text by detecting relevant n-grams  and calculating its polarity. 

An n-gram is a collection of n successive items in a text document that may include words, numbers, symbols, and punctuation. 
N-gram models are useful in many text analytics applications where sequences of words are relevant, such as in sentiment analysis, text classification, and text generation.

The advantage of using n-grams is that we analyse words within a context instead of as separate words.

Still analysing words as n-grams may be susceptible to not correctly describing colloquial expressions in which the words have a different meaning.
 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
