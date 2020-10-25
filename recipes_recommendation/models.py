from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

from recipes_recommendation import dataset


def train_outlier_classifier(dataframe, **kwargs):
    classifier = IsolationForest(**kwargs)
    classifier.fit(dataframe)
    return classifier


def train_cluster_model(dataframe):
    model = KMeans(n_clusters=8, random_state=0)
    return model.fit(dataframe[dataset.FEATURE_COLUMNS])
