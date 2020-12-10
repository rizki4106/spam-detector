from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from .distance import distance
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

    def sort_data(self,data):
        return data['distance']

    def get_similary(self, message_predict):
        """
        return similar data between actual data and the data that will be predicted
        """

        vector = TfidfVectorizer()
        # set the old data
        message = pd.DataFrame(self.dataset)
        new_message = pd.Series({
            "message": message_predict,
            "type": "new"
        })
        # merge old data with new data
        new_data = message.append(new_message, ignore_index=True)

        # create vector
        message_transform = vector.fit_transform(new_data.iloc[:,0]).toarray()

        # calculate distance between new data and old data
        data_distance = []
        for i in range(0, len(message_transform)):
            list_result = {}
            list_result['distance'] = distance.euclidean(message_transform[len(message_transform) - 1], message_transform[i])
            list_result['index'] = i
            data_distance.append(list_result)
        
        # sorting the data from the nearest distance
        data_distance.sort(key=self.sort_data)

        # get the data from the nearest distance
        similar_message = []
        for i in range(0,5):
            similar_message.append(new_data.iloc[:,0].values[data_distance[i]['index']])

        # return the data
        return similar_message

    def predict(self, message):
        """
        predict a new message
        """
        predict = self.run_classification(message)
        similarity = self.get_similary(message)
        return {
            "prediction" :predict,
            "similarity": similarity
        }

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