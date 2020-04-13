# Exploring differences in language usage in customer reviews on weekends vs weekdays
### CS7IS4-Group6 Project
##### Adhishwar Singh Mittal, Piyush Saxena, Srijan Roy, Sujit Jadhav, Vishal Kumar
amittal@tcd.ie, psaxena@tcd.ie, roysr@tcd.ie, kumarv1@tcd.ie    
**Keywords**: amazon reviews, timecycle, language usage, Tree SHAP, count vectors, parts of speech, ZipF score, feature extraction, text complexity, point-biserial, Kruskal-Wallis

>It is often seen on online platforms that customers have different behaviours with respect to browsing, shopping or spending at different points of time. For an online food ordering service, customers are more active during dinner as compared to breakfast, or more active on weekends than weekdays. Similarly, for online merchandise stores, customers are more active during festive seasons. This makes us think, can their behaviour while writing reviews on these platforms also vary? And hence, the research question, can we identify patterns of language usage across different time cycles? In this paper we attempt to find differences in language usage in amazon reviews on weekends vs weekdays. We study the frequency of words and complexity of language to explain the correlation between review texts and the day on which the review was posted being a weekday or a weekend.

## Content Description
The folder consists of 2 folders:
1. Hypothesis Test which consists of the 1st step of the work:
We conduct a primary test to prove that the text of the reviews hold valid correlation with the text being written on a weekend or weekday. A permutation test is used to rank model accuracy from a permutation of randomly distributed labels. 
2. Model Evaluation and Explanation:
This step consists of undertsanding the model predictions to explain the predictability through text.

## Model Results

1. The model has an AUC of 0.71
![Model ROC](https://github.com/amittal-tcd/TCD-work/blob/master/Text%20Analytics/Step2%20-%20Model%20Improvement%20and%20Feature%20Importances/Results/ROC.png)

2. The model has a precision of 0.81 and a recall of 0.96
![Model Confusion Matrix](https://github.com/amittal-tcd/TCD-work/blob/master/Text%20Analytics/Step2%20-%20Model%20Improvement%20and%20Feature%20Importances/Results/Confusion%20Matrix.png)

3. The most important features are as shown below
![Model Feature Importances](https://github.com/amittal-tcd/TCD-work/blob/master/Text%20Analytics/Step2%20-%20Model%20Improvement%20and%20Feature%20Importances/Results/LGBMImportances.JPG)

4. Model is explained using SHAP values as shown by the summary below
![Model SHAP Values](https://github.com/amittal-tcd/TCD-work/blob/master/Text%20Analytics/Step2%20-%20Model%20Improvement%20and%20Feature%20Importances/Results/Summary%20100%20Features.png)
