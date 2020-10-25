import seaborn as sns

from recipes_recommendation import dataset


def feature_histogram(dataframe, output_path, feature_column):
    plot = sns.histplot(data=dataframe, x=feature_column, bins=50)
    figure = plot.get_figure()
    figure.savefig(output_path + 'histogram_' + feature_column + '.png')
    figure.clf()


def classes_histogram(dataframe, output_path):
    plot = sns.histplot(data=dataframe, x=dataset.LABEL_COLUMN)
    figure = plot.get_figure()
    figure.savefig(output_path + 'histogram_classes.png')
    figure.clf()
