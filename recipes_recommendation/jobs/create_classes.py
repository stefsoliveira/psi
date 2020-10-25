#!/usr/bin/env python3
import logging
import sys

import pandas as pd

from recipes_recommendation import dataset, models, validation

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    dataset_path = str(sys.argv[1])
    output_path = str(sys.argv[2])
    LOG.info("Starting job: %s", __name__)

    LOG.info("Loading dataset from: %s", dataset_path)
    dataframe = pd.read_csv(dataset_path)
    LOG.info("Done loading dataset")

    LOG.info("Start training clustering model")
    clustering_model = models.train_cluster_model(dataframe)
    LOG.info("Start training clustering model")

    LOG.info("Start classifying")
    classes = clustering_model.predict(dataframe[dataset.NUTRITION_COLUMNS])
    dataframe_with_classes = dataframe.copy()
    dataframe_with_classes['class'] = classes
    LOG.info("Done classifying")

    LOG.info("Start saving dataset with classes to: %s", output_path)
    dataframe_with_classes.to_csv(output_path + 'recipe_features_with_classes.csv', index=False)
    LOG.info("Done saving dataset with classes")

    LOG.info("Start creating histogram of distribution of classes in: %s", output_path)
    validation.classes_histogram(dataframe_with_classes, output_path)
    LOG.info("Done creating histogram of distribution of classes")

    LOG.info("Finishing job")
