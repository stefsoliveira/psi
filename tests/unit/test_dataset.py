import pandas as pd
import pandas.testing as pdt

from recipes_recommendation import dataset


def test_should_explode_nutrition_column():
    data = [[20, "[269.8, 22.0, 32.0, 48.0, 39.0, 27.0, 5.0]"]]
    df = pd.DataFrame(data, columns=['id', 'nutrition'])

    actual = dataset.extract_features(df)
    expected = pd.DataFrame(
        [[20, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]],
        columns=['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )

    pdt.assert_frame_equal(expected, actual)


def test_should_explode_nutrition_column_ignore_other_columns():
    data = [[
        20,
        "bar",
        "[1, 2.0, 12.0, 42.0, 3.7, 1337.0, 5.0]"
    ]]
    df = pd.DataFrame(data, columns=['id', "foo", 'nutrition'])

    actual = dataset.extract_features(df)
    expected = pd.DataFrame(
        [[1.0, 2.0, 12.0, 42.0, 3.7, 1337.0, 5.0]],
        columns=['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )

    pdt.assert_frame_equal(expected, actual)


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
