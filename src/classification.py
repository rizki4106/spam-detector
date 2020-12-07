from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

class FilterMessage:
    """
    This class used for classifying a message as a spam or ham
    """

    def __init__(self):
        self.message = []
        self.lable = []

    def run_classification(self, predict_value):
        """
        Run classification using K-Neirest Neighbors Algorthm
        """
        dataset = pd.read_json("./data/message.json");
        x = dataset.iloc[:, 0].values
        y = dataset.iloc[:, -1].values

        # Term Weighting

        vector = TfidfVectorizer()
        transform_x = vector.fit_transform(x).toarray()

        # KNN
        algorithm = KNeighborsClassifier(n_neighbors=1, metric="euclidean", algorithm="brute")
        algorithm.fit(transform_x, y)
        prediction_message = pd.Series([predict_value])

        # Term Weighting
        transform_message = vector.transform(prediction_message).toarray()
        return algorithm.predict(transform_message)

    def predict(self, message):
        """
        predict a new message
        """
        return self.run_classification(message)


if __name__ != "__main__":
    filter = FilterMessage()