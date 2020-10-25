#!/usr/bin/env python3
import logging
import sys

import pandas as pd

from recipes_recommendation import dataset, validation

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    dataset_path = str(sys.argv[1])
    output_path = str(sys.argv[2])
    LOG.info("Starting job: %s", __name__)

    LOG.info("Start loading features dataset from: %s", dataset_path)
    dataframe = pd.read_csv(dataset_path)
    LOG.info("Done loading features dataset")

    LOG.info("Start creating histograms in: %s", output_path)
    for feature_column in dataset.NUTRITION_COLUMNS:
        LOG.info("Start creating histogram for: %s", feature_column)
        validation.feature_histogram(dataframe, output_path, feature_column)
        LOG.info("Done creating histogram")
    LOG.info("Done creating histograms")
    LOG.info("Finishing job")
