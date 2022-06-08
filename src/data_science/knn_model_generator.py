import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

def load_dataset():
    return datasets.load_iris()

def get_training_data(dataset):
    data = dataset.data
    target = dataset.target
    return train_test_split(data, target, test_size=0.35)

def get_trained_model(data_train, target_train):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(data_train, target_train)
    return knn

def validate_model(model, data_test, target_test):
    predicted = model.predict(data_test)
    print(f"Model Accuracy: {metrics.accuracy_score(target_test, predicted)}")

def save_model(model):
    with open('iris.knn.model', 'wb') as file:
        pickle.dump(model, file)

def main():
    dataset = load_dataset()
    data_train, data_test, target_train, target_test = get_training_data(dataset)
    model = get_trained_model(data_train, target_train)
    validate_model(model, data_test, target_test)
    save_model(model)

main()