#!/usr/bin/env python3
import logging
import sys

import pandas as pd

from recipes_recommendation import dataset, models

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    dataset_path = str(sys.argv[1])
    output_path = str(sys.argv[2])
    LOG.info("Starting job: %s", __name__)

    LOG.info("Loading dataset from: %s", dataset_path)
    raw_dataframe = pd.read_csv(dataset_path)
    features = raw_dataframe[dataset.FEATURE_COLUMNS]
    LOG.info("Done loading dataset")

    LOG.info("Start training outlier classifier")
    classifier = models.train_outlier_classifier(features, n_estimators=30)
    LOG.info("Done training outlier classifier")

    LOG.info("Start marking outliers")
    with_outliers_marked = dataset.with_outliers_column(classifier, raw_dataframe)
    LOG.info("Done marking outliers")

    LOG.info("Start saving features with and without outliers to: %s", output_path)
    without_outliers = with_outliers_marked[with_outliers_marked[dataset.OUTLIER_COLUMN] == 1]
    without_outliers.to_csv(output_path + 'recipe_features_without_outliers.csv', index=False)
    only_outliers = with_outliers_marked[with_outliers_marked[dataset.OUTLIER_COLUMN] == -1]
    only_outliers.to_csv(output_path + 'recipe_features_only_outliers.csv', index=False)
    LOG.info("Done saving features with and without outliers")

    LOG.info("Finishing job")
