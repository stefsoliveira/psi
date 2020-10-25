#!/usr/bin/env python3
import logging
import sys

import pandas as pd

from recipes_recommendation import dataset, models, validation

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    training_dataset_path = str(sys.argv[1])
    predict_dataset_path = str(sys.argv[2])
    output_path = str(sys.argv[3])
    LOG.info("Starting job: %s", __name__)

    LOG.info("Loading datasets from: %s, %s", training_dataset_path, predict_dataset_path)
    train_dataset = pd.read_csv(training_dataset_path)
    predict_dataset = pd.read_csv(predict_dataset_path)
    LOG.info("Done loading dataset")

    LOG.info("Start training clustering model")
    clustering_model = models.train_cluster_model(train_dataset)
    LOG.info("Start training clustering model")

    LOG.info("Start classifying")
    classes = clustering_model.predict(predict_dataset[dataset.FEATURE_COLUMNS])
    dataframe_with_classes = predict_dataset.copy()
    dataframe_with_classes[dataset.LABEL_COLUMN] = classes
    LOG.info("Done classifying")

    LOG.info("Start saving dataset with classes to: %s", output_path)
    dataframe_with_classes[[dataset.ID_COLUMN, dataset.LABEL_COLUMN]] \
        .to_csv(output_path + 'recipe_features_with_labels.csv', index=False)
    LOG.info("Done saving dataset with classes")

    LOG.info("Start creating histogram of distribution of classes in: %s", output_path)
    validation.classes_histogram(dataframe_with_classes, output_path)
    LOG.info("Done creating histogram of distribution of classes")

    LOG.info("Finishing job")
