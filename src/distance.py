import numpy as np

class DistanceClassifier:
    """
    distance formula
    """

    def euclidean(self, x, y):
        a = np.array(x)
        b = np.array(y)
        c = np.sum(np.square(a - b))
        return np.sqrt(c)


if __name__ != "__main__":
    distance = DistanceClassifier()