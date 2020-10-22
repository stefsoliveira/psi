import pandas as pd
import pandas.testing as pdt

from recipes_recommendation import dataset


def test_should_return_1_for_single_value():
    dataframe = pd.DataFrame([[42.0]], columns=['foo'])

    actual = dataset.normalize_nominal('foo', dataframe)
    expected = pd.DataFrame([[1.0]], columns=['normalized_foo'])

    pdt.assert_frame_equal(expected, actual)


def test_should_normalize_n_rows():
    dataframe = pd.DataFrame([[42.0], [1.0], [21.0]], columns=['foo'])

    actual = dataset.max_value('foo', dataframe)
    expected = pd.DataFrame([[1.0], [1.0 / 42.0], [21.0 / 42.0]], columns=['normalized_foo'])

    pdt.assert_frame_equal(expected, actual)


def test_should_normalize_n_rows_with_n_columns():
    dataframe = pd.DataFrame(
        [
            [1.0, 100.0],
            [1.0, 50.0],
            [21.0, 10.0]
        ],
        columns=['foo', 'bar']
    )

    actual = dataset.max_value('bar', dataframe)
    expected = pd.DataFrame(
        [
            [1.0, 100.0 / 100.0],
            [1.0, 50.0 / 100.0],
            [21.0, 10.0 / 100.0]
        ],
        columns=['foo', 'normalized_bar']
    )

    pdt.assert_frame_equal(expected, actual)
