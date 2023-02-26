import pickle

import numpy


def evaluate_probs(data):
    X = numpy.array(data)

    print("x: " + str(X))

    with open("model.pickle", "rb") as pickle_in:
        model = pickle.load(pickle_in)

    print("Test 1")
    prediction = model.predict(X)
    print("Test 2")

    return prediction
