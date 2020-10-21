import pandas as pd

from recipes_recommendation import dataset


def test_should_map_one_user_to_index():
    df = pd.DataFrame({'user_id': [1337]})

    actual = dataset.user_index_map(df)
    expected = {1337: 0}

    assert expected == actual


def test_should_map_n_users_to_indices():
    df = pd.DataFrame({'user_id': [1337, 24, 42]})

    actual = dataset.user_index_map(df)
    expected = {
        24: 0,
        42: 1,
        1337: 2,
    }

    assert expected == actual
