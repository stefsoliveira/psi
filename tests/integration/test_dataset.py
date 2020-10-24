import pandas as pd
import pandas.testing as pdt

from recipes_recommendation import dataset


def test_should_extract_features_from_file():
    dataframe = pd.read_csv('tests/integration/resources/raw_recipes_dump.csv')

    actual = dataset.extract_features(dataframe)
    expected = pd.DataFrame(
        [
            [137739.0, 51.5, 0.0, 13.0, 0.0, 2.0, 0.0],
            [31490.0, 173.4, 18.0, 0.0, 17.0, 22.0, 35.0],
            [112140.0, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]
        ],
        columns=['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']
    )

    pdt.assert_frame_equal(expected, actual)


def test_should_normalize():
    dataframe = pd.read_csv('tests/integration/resources/raw_recipes_dump.csv')
    extracted_features = dataset.extract_features(dataframe)
    normalize_columns = ['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']

    actual = dataset.normalize(normalize_columns, extracted_features)
    expected = pd.DataFrame(
        [
            [137739.0, 51.5 / 269.8, 0.0 / 22.0, 13.0 / 32.0, 0.0 / 48.0, 2.0 / 39.0, 0.0 / 35.0],
            [31490.0, 173.4 / 269.8, 18.0 / 22.0, 0.0 / 32.0, 17.0 / 48.0, 22.0 / 39.0, 35.0 / 35.0],
            [112140.0, 269.8 / 269.8, 22.0 / 22.0, 32.0 / 32.0, 48.0 / 48.0, 39.0 / 39.0, 27.0 / 35.0]
        ],
        columns=[
            'id',
            'normalized_calories',
            'normalized_total_fat',
            'normalized_sugar',
            'normalized_sodium',
            'normalized_protein',
            'normalized_saturated_fat'
        ]
    )

    pdt.assert_frame_equal(expected, actual)
