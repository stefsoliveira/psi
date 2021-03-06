# psi

## Prerequisites
This project uses pipenv to manage the dependencies and some build steps
in order to keep track of specific versions.

Please make sure you have installed:
* [pipenv](https://pipenv.pypa.io/en/latest/)
* [pyenv](https://github.com/pyenv/pyenv)

## Install all dependencies
```bash
pipenv run install --dev
```

## Run tests
To run all the tests:
```bash
pipenv run test
```

### Run unit-tests
```bash
pipenv run unit-tests
```

### Run integration-tests
```bash
pipenv run integration-tests
```

## Run linter
```bash
pipenv run linter
```

## Run dev server
Make sure you have run the full pipeline first (`make run-full-pipeline`)
Will start dev server on port `8080`
```bash
pipenv run dev-server
```

## Jobs
There are multiple jobs in the `./recipes_recommendation/jobs` folder.
To run them execute them with `pipenv run ...`

Or you can run them with make:

```bash
make run-data-preprocessing-pipeline # runs only all data preprocessing steps (including outlier detection)
make run-train-pipeline # runs only the cluster model training and applies it to all data
make run-full-pipeline # runs the whole pipeline with data preprocessing and training the cluster model/classifier
```

### Extracting features
To extract the features out of the raw dataset:
```bash
pipenv run recipes_recommendation/jobs/extract_features.py $INPUT_FILE $OUTPUT_FOLDER
```

#### Input
RAW recipes csv file looking like:
```csv
name,id,minutes,contributor_id,submitted,tags,nutrition,n_steps,steps,description,ingredients,n_ingredients
arriba   baked winter squash mexican style,137739,55,47892,2005-09-16,"['60-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'cuisine', 'preparation', 'occasion', 'north-american', 'side-dishes', 'vegetables', 'mexican', 'easy', 'fall', 'holiday-event', 'vegetarian', 'winter', 'dietary', 'christmas', 'seasonal', 'squash']","[51.5, 0.0, 13.0, 0.0, 2.0, 0.0, 4.0]",11,"['make a choice and proceed with recipe', 'depending on size of squash , cut into half or fourths', 'remove seeds', 'for spicy squash , drizzle olive oil or melted butter over each cut squash piece', 'season with mexican seasoning mix ii', 'for sweet squash , drizzle melted honey , butter , grated piloncillo over each cut squash piece', 'season with sweet mexican spice mix', 'bake at 350 degrees , again depending on size , for 40 minutes up to an hour , until a fork can easily pierce the skin', 'be careful not to burn the squash especially if you opt to use sugar or butter', 'if you feel more comfortable , cover the squash with aluminum foil the first half hour , give or take , of baking', 'if desired , season with salt']","autumn is my favorite time of year to cook! two of my posted mexican-inspired seasoning mix recipes are offered as suggestions.","['winter squash', 'mexican seasoning', 'mixed spice', 'honey', 'butter', 'olive oil', 'salt']",7
a bit different  breakfast pizza,31490,30,26278,2002-06-17,"['30-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'cuisine', 'preparation', 'occasion', 'north-american', 'breakfast', 'main-dish', 'pork', 'american', 'oven', 'easy', 'kid-friendly', 'pizza', 'dietary', 'northeastern-united-states', 'meat', 'equipment']","[173.4, 18.0, 0.0, 17.0, 22.0, 35.0, 1.0]",9,"['preheat oven to 425 degrees f', 'press dough into the bottom and sides of a 12 inch pizza pan', 'bake for 5 minutes until set but not browned', 'cut sausage into small pieces', 'whisk eggs and milk in a bowl until frothy', 'spoon sausage over baked crust and sprinkle with cheese', 'pour egg mixture slowly over sausage and cheese', 's& p to taste', 'bake 15-20 minutes or until eggs are set and crust is brown']",this recipe calls for the crust to be prebaked a bit before adding ingredients. feel free to change sausage to ham or bacon. this warms well in the microwave for those late risers.,"['prepared pizza crust', 'sausage patty', 'eggs', 'milk', 'salt and pepper', 'cheese']",6
all in the kitchen  chili,112140,130,196586,2005-02-25,"['time-to-make', 'course', 'preparation', 'main-dish', 'chili', 'crock-pot-slow-cooker', 'dietary', 'equipment', '4-hours-or-less']","[269.8, 22.0, 32.0, 48.0, 39.0, 27.0, 5.0]",6,"['brown ground beef in large pot', 'add chopped onions to ground beef when almost brown and sautee until wilted', 'add all other ingredients', 'add kidney beans if you like beans in your chili', 'cook in slow cooker on high for 2-3 hours or 6-8 hours on low', 'serve with cold clean lettuce and shredded cheese']",this modified version of 'mom's' chili was a hit at our 2004 christmas party. we made an extra large pot to have some left to freeze but it never made it to the freezer. it was a favorite by all. perfect for any cold and rainy day. you won't find this one in a cookbook. it is truly an original.,"['ground beef', 'yellow onions', 'diced tomatoes', 'tomato paste', 'tomato soup', 'rotel tomatoes', 'kidney beans', 'water', 'chili powder', 'ground cumin', 'salt', 'lettuce', 'cheddar cheese']",13
...
```

#### Output
`recpie_features.csv` CSV file with only nutrition features and id looking like: 
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat
137739.0,51.5,0.0,13.0,0.0,2.0,0.0
31490.0,173.4,18.0,0.0,17.0,22.0,35.0
...
```

### Removing outliers
To remove outliers from the features:
```bash
pipenv run recipes_recommendation/jobs/remove_outliers.py $INPUT_FILE $OUTPUT_FOLDER
```

#### Input
`recpie_features.csv` CSV file with only nutrition features and id looking like:
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat
137739.0,51.5,0.0,13.0,0.0,2.0,0.0
31490.0,173.4,18.0,0.0,17.0,22.0,35.0
...
```

#### Output
Two files, `recipe_features_only_outliers.csv` and `recipe_features_without_outliers.csv`.
`recipe_features_without_outliers.csv` CSV file without any outliers: 
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat,outlier
137739.0,51.5,0.0,13.0,0.0,2.0,0.0,1
31490.0,173.4,18.0,0.0,17.0,22.0,35.0,1
112140.0,269.8,22.0,32.0,48.0,39.0,27.0,1
...
```

`recipe_features_only_outliers.csv` CSV file only with outliers: 
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat,outlier
67888.0,1109.5,83.0,378.0,275.0,96.0,86.0,-1
70971.0,4270.8,254.0,1306.0,111.0,127.0,431.0,-1
75452.0,2669.3,160.0,976.0,107.0,62.0,310.0,-1
...
```

### Create histograms of features and their distribution
To create histograms for each feature and its distribution:
```bash
pipenv run recipes_recommendation/jobs/create_histograms.py $INPUT_FILE $OUTPUT_FOLDER
```

#### Input
feature recipes csv file looking like:
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat
137739.0,51.5,0.0,13.0,0.0,2.0,0.0
31490.0,173.4,18.0,0.0,17.0,22.0,35.0
112140.0,269.8,22.0,32.0,48.0,39.0,27.0
...
```

#### Output
`histogram_$FEATURE_NAME.png` png file with the histogram for the `$FEATURE_NAME`.

### Train and classify all recipes
To train a clustering classifier for the recipes:
```bash
pipenv run recipes_recommendation/jobs/train_and_classify.py $TRAIN_DATA $PREDICTION_DATA $OUTPUT_FOLDER
```

#### Input
Will take `$TRAIN_DATA` and `$PREDICTION_DATA` csv files to train and predict the labels.

`$TRAIN_DATA` csv file for training the cluster classifier looking like:
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat
137739.0,51.5,0.0,13.0,0.0,2.0,0.0
31490.0,173.4,18.0,0.0,17.0,22.0,35.0
112140.0,269.8,22.0,32.0,48.0,39.0,27.0
...
```

`$PREDICTION_DATA` csv file for training the cluster classifier looking like:
```csv
id,calories,total_fat,sugar,sodium,protein,saturated_fat
137739.0,51.5,0.0,13.0,0.0,2.0,0.0
31490.0,173.4,18.0,0.0,17.0,22.0,35.0
112140.0,269.8,22.0,32.0,48.0,39.0,27.0
...
```

#### Output
`recipe_id_with_labels.csv` CSV file looking like:
```csv
id,label
137739.0,4
31490.0,6
...
```
