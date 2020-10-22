import pandas as pd
import pandas.testing as pdt

from recipes_recommendation import dataset


def test_should_extract_features_from_file():
    dataframe = pd.read_csv('tests/integration/resources/raw_recipes_dump.csv')

    actual = dataset.extract_features(dataframe)
    expected = pd.DataFrame(
        [
            [137739, 51.5, 0.0, 13.0, 0.0, 2.0, 0.0],
            [31490, 173.4, 18.0, 0.0, 17.0, 22.0, 35.0],
            [112140, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]
        ],
        columns=['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )

    pdt.assert_frame_equal(expected, actual)
