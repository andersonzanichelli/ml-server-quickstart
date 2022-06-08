import json
import time
import pickle
import numpy as np

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

def init():
    time.sleep(1)

def load_model():
    with open('iris.knn.model', 'rb') as file:
        return pickle.load(file)

def build_np_array(data):
    irisData = json.loads(data)
    return np.array([[
            float(irisData["feat1"]), 
            float(irisData["feat2"]), 
            float(irisData["feat3"]), 
            float(irisData["feat4"])]])

def predict(data):
    return load_model().predict(data)

def run(data):
    result = predict(build_np_array(data))

    return {
        "model": "knn",
        "prediction": str(result),
        "name": species[result[0]]
        }