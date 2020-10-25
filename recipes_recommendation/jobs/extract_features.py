#!/usr/bin/env python3
import logging
import sys

import pandas as pd

from recipes_recommendation import dataset

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    dataset_path = str(sys.argv[1])
    output_path = str(sys.argv[2])
    LOG.info("Starting job: %s", __name__)

    LOG.info("Loading dataset from: %s", dataset_path)
    raw_dataframe = pd.read_csv(dataset_path)
    LOG.info("Done loading dataset")

    LOG.info("Start extracting features")
    features_dataframe = dataset.extract_features(raw_dataframe)
    LOG.info("Done extracting features")

    LOG.info("Start saving features to: %s", output_path)
    features_dataframe.to_csv(output_path + 'recipe_features.csv', index=False)
    LOG.info("Done saving features")

    LOG.info("Finishing job")
