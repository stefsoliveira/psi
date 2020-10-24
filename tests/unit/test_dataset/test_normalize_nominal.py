import pandas as pd
import pandas.testing as pdt

from recipes_recommendation import dataset


def test_should_return_1_for_single_value():
    dataframe = pd.DataFrame([[42.0]], columns=['foo'])

    actual = dataset.normalize_nominal(dataframe, 'foo')
    expected = pd.DataFrame([[1.0]], columns=['normalized_foo'])

    pdt.assert_frame_equal(expected, actual)


def test_should_normalize_n_rows():
    dataframe = pd.DataFrame([[42.0], [1.0], [21.0]], columns=['foo'])

    actual = dataset.normalize_nominal(dataframe, 'foo')
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

    actual = dataset.normalize_nominal(dataframe,'bar')
    expected = pd.DataFrame(
        [
            [1.0, 100.0 / 100.0],
            [1.0, 50.0 / 100.0],
            [21.0, 10.0 / 100.0]
        ],
        columns=['foo', 'normalized_bar']
    )

    pdt.assert_frame_equal(expected, actual)


def test_should_do_nothing_if_max_value_is_0():
    dataframe = pd.DataFrame([[0.0], [0.0]], columns=['foo'])

    actual = dataset.normalize_nominal(dataframe,'foo')
    expected = pd.DataFrame([[0.0], [0.0]], columns=['normalized_foo'])

    pdt.assert_frame_equal(expected, actual)
