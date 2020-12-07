# spam-detector
Detect messages *(message in indonesian language)* as spam or not by implementing machine learning algorithms
## Description
This program made for classifying text messages to be spam or ham. To implement text into machine learning algorithm we calculate the **TF - IDF** *(term frequency inverse document frequency)* and than to detect spam or ham we use **K - Nearest Neighbor** algorithm we calculate the TF-IDF based on nearest data

## Dataset
The data that we used for predict message located in *data/message.json*, we need more data to make this programs more perfect
## Performance
From 17 rows data set we used 70% as training data and 30% as testing data

Confusion Matrix
![](https://i.postimg.cc/D0MHYgwd/confusion-matrix.png)
```bash
              precision    recall  f1-score   support

         ham       1.00      1.00      1.00         1
        spam       1.00      1.00      1.00         5

   accuracy                            1.00         6
   macro avg       1.00      1.00      1.00         6
   weighted avg    1.00      1.00      1.00         6
```
## Installation
```bash
git clone https://github.com/rizki4106/spam-detector.git
```
```bash
cd spam-detector && pip3 install -r requirements.txt
```
```bash
open main.py
```
```python
from src import filter

msg = input("Masukan pesan : ")

print(filter.predict(msg))
```

```bash
python3 main.py
```