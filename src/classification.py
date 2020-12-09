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
        self.dataset = ''

    def run_classification(self, predict_value):
        """
        Run classification using K-Neirest Neighbors Algorthm
        """
        dataset = pd.read_csv("./data/message.csv")
        self.dataset = dataset
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

    def fit(self, message, type):
        """
        fit and write new data
        """

        data_frame = pd.DataFrame(self.dataset)
        new_data = {
            "message": message,
            "type": type
        }
        new_file = data_frame.append(new_data, ignore_index=True)
        new_file.to_csv("data/message.csv", index=False)

if __name__ != "__main__":
    filter = FilterMessage()