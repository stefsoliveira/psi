# coding=utf-8
import logging
import threading

import pandas as pd
from flask import Flask, request

from recipes_recommendation import dataset

LOG = logging.getLogger(__name__)
APP = Flask(__name__)

_DATABASE = None
_DATABASE_LOCK = threading.RLock()


def _load_database():
    recipes = pd.read_csv('./resources/RAW_recipes.csv')
    LOG.debug(recipes)
    labels = pd.read_csv('./resources/recipe_id_with_labels.csv')
    LOG.debug(labels)
    recipes_with_labels = pd.merge(recipes, labels, on=dataset.ID_COLUMN)
    LOG.debug(recipes_with_labels)
    return recipes_with_labels


def database():
    global _DATABASE
    if not _DATABASE:
        LOG.info("Loading database")
        with _DATABASE_LOCK:
            _DATABASE = _load_database()
    return _DATABASE


@APP.route('/health')
def health():
    return {'status': '😀'}


def __is_valid_request(query_params):
    return query_params.get('class')


@APP.route('/recipes', methods=['GET'])
def ping():
    if not __is_valid_request(request.args):
        LOG.info('No class param present')
        return {'error': 'class is not present'}, 400

    recipe_class = int(request.args.get('class'))
    all_recipes = database()
    recipes_with_label = all_recipes[all_recipes[dataset.LABEL_COLUMN] == recipe_class]
    LOG.debug(recipes_with_label)
    return recipes_with_label.T.to_dict().values()
