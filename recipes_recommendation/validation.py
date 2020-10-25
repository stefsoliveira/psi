import seaborn as sns


def feature_histogram(dataframe, output_path, feature_column):
    plot = sns.histplot(data=dataframe, x=feature_column, bins=50)
    figure = plot.get_figure()
    figure.savefig(output_path + 'histogram_' + feature_column + '.png')
    figure.clf()
