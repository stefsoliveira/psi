import logging

import seaborn as sns

LOG = logging.getLogger(__name__)


def feature_histogram(dataframe, output_path, feature_column):
    LOG.info(feature_column)
    plot = sns.histplot(data=dataframe, x=feature_column, bins=50)
    figure = plot.get_figure()
    figure.savefig(output_path + 'histogram_' + feature_column + '.png')
    figure.clf()
