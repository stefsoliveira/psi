from sklearn.ensemble import IsolationForest


def train_outlier_classifier(dataframe, **kwargs):
    classifier = IsolationForest(**kwargs)
    classifier.fit(dataframe)
    return classifier
