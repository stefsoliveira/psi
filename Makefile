OUTPUT_FOLDER = "./resources/"
RAW_DATASET = $(OUTPUT_FOLDER)"RAW_recipes.csv"
FEATURES_DATASET = $(OUTPUT_FOLDER)"recipe_features.csv"
WITHOUT_OUTLIERS_DATASET = $(OUTPUT_FOLDER)"recipe_features_without_outliers.csv"

.PHONY: run-extract-features
run-extract-features:
	pipenv run recipes_recommendation/jobs/extract_features.py $(RAW_DATASET) $(OUTPUT_FOLDER)

.PHONY: run-remove-outliers
run-remove-outliers:
	pipenv run recipes_recommendation/jobs/remove_outliers.py $(FEATURES_DATASET) $(OUTPUT_FOLDER)

.PHONY: run-create-histograms
run-create-histograms:
	pipenv run recipes_recommendation/jobs/create_histograms.py $(WITHOUT_OUTLIERS_DATASET) $(OUTPUT_FOLDER)

.PHONY: run-train-and-classify
run-train-and-classify:
	pipenv run recipes_recommendation/jobs/train_and_classify.py $(WITHOUT_OUTLIERS_DATASET) $(FEATURES_DATASET) $(OUTPUT_FOLDER)

.PHONY: run-data-preprocessing-pipeline
run-data-preprocessing-pipeline: run-extract-features run-remove-outliers run-create-histograms

.PHONY: run-train-pipeline
run-train-pipeline: run-train-and-classify

.PHONY: run-full-pipeline
run-full-pipeline: run-data-preprocessing-pipeline run-train-and-classify


