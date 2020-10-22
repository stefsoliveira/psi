import pandas as pd


def extract_features(dataframe):
    return pd.DataFrame(
        [
            [20, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]
        ],
        ['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )


def max_value(column_name, dataframe):
    # order column by max value desc
    # select first row
    # return first row
    pass


def normalize_nominal(column_name, dataframe):
    # calculate max_value for column and save as max
    # create new column and name it normalized_$column_name
    # copy old column data into the new column
    # apply function on each row in the new column: row / max (hint: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
    # return dataframe that has the new column and not the old one
    pass
