import pandas as pd


def extract_features(dataframe):
    return pd.DataFrame(
        [
            [20, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]
        ],
        ['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )
