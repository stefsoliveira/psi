import pandas as pd

from recipes_recommendation import dataset


def test_should_calculate_max_number_for_only_one_field():
    dataframe = pd.DataFrame([[42.0]], columns=['foo'])

    actual = dataset.max_value('foo', dataframe)
    expected = 42.0

    assert expected == actual


def test_should_calculate_max_number_n_rows():
    dataframe = pd.DataFrame([[42.0], [1337.0]], columns=['foo'])

    actual = dataset.max_value('foo', dataframe)
    expected = 1337.0

    assert expected == actual


def test_should_calculate_max_number_for_multiple_max_values():
    dataframe = pd.DataFrame([[42.0], [42.0]], columns=['foo'])

    actual = dataset.max_value('foo', dataframe)
    expected = 42.0

    assert expected == actual


def test_should_calculate_max_number_for_multiple_columns():
    dataframe = pd.DataFrame([[123.0, 1337.0], [2.0, 9000.0]], columns=['foo', 'bar'])

    actual = dataset.max_value('bar', dataframe)
    expected = 9000.0

    assert expected == actual
