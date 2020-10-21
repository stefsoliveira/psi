import pandas as pd
from recipes_recommendation import dataset

def test_should_explode_nutrition_column():
    data = [
        20,
        "[269.8, 22.0, 32.0, 48.0, 39.0, 27.0, 5.0]"
    ]
    df = pd.DataFrame(data, columns = ['id', 'nutrition']) 
    
    actual = dataset.extract_features(df)
    expected = pd.DataFrame([20, 269.8, 22.0, 32.0, 48.0, 39.0, 27.0]], columns = ['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']) 
    
    assert expected == actual


def test_should_explode_nutrition_column_ignore_other_columns():
    data = [
        20,
        "bar",
        "[269.8, 22.0, 32.0, 48.0, 39.0, 1337.0, 5.0]"
    ]
    df = pd.DataFrame(data, columns = ['id', "foo",'nutrition']) 
    
    actual = dataset.extract_features(df)
    expected = pd.DataFrame([20, 269.8, 22.0, 32.0, 48.0, 39.0, 1337.0]], columns = ['id', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat']) 
    
    assert expected == actual


