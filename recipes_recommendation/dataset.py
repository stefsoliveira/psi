import json
from functools import partial, reduce

import pandas as pd
from sklearn.ensemble import IsolationForest

NUTRITION_COLUMN = 'nutrition'
NUTRITION_COLUMNS = ['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
ID_COLUMN = 'id'


def explode_nutrition_data(row):
    nutrition_data = json.loads(row[NUTRITION_COLUMN])
    exploded_row = [row[ID_COLUMN]] + nutrition_data[:-1]
    return pd.Series(
        exploded_row,
        [ID_COLUMN] + NUTRITION_COLUMNS
    )


def extract_features(dataframe):
    only_id_and_nutrition = dataframe[[ID_COLUMN, NUTRITION_COLUMN]]
    with_exploded_nutrition_data = only_id_and_nutrition.apply(explode_nutrition_data, axis=1)
    return with_exploded_nutrition_data


def max_value(column_name, dataframe):
    sorted_by_column = dataframe.sort_values(by=[column_name], ascending=False)
    return sorted_by_column.iloc[0][column_name]


def normalize_nominal_row(column_name, highest_value, row):
    normalized_row = row.copy()
    if highest_value > 0:
        normalized_row['normalized_' + column_name] = row[column_name] / highest_value
    else:
        normalized_row['normalized_' + column_name] = row[column_name]
    del normalized_row[column_name]
    return normalized_row


def normalize_nominal(dataframe, column_name):
    max_column_value = max_value(column_name, dataframe)
    normalize_fn = partial(normalize_nominal_row, column_name, max_column_value)
    with_normalized_column = dataframe.apply(normalize_fn, axis=1)
    return with_normalized_column


def normalize(to_normalize_column_names, dataframe):
    return reduce(normalize_nominal, to_normalize_column_names, dataframe)


def train_outlier_classifier(dataframe, **kwargs):
    classifier = IsolationForest(**kwargs)
    classifier.fit(dataframe)
    return classifier


def with_outliers_column(classifier, dataframe):
    with_column_added = dataframe.copy()
    outliers = classifier.predict(dataframe[NUTRITION_COLUMNS])
    with_column_added['outlier'] = outliers
    return with_column_added
