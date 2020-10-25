# coding=utf-8
import logging
import random
import threading

import pandas as pd
from flask import Flask, request

from recipes_recommendation import dataset

LOG = logging.getLogger(__name__)
APP = Flask(__name__)

_DATABASE = None
_DATABASE_LOCK = threading.RLock()


def _load_database():
    recipes = pd.read_csv('./resources/RAW_recipes.csv').sort_values(by=[dataset.ID_COLUMN])
    labels = pd.read_csv('./resources/recipe_id_with_labels.csv').sort_values(by=[dataset.ID_COLUMN])
    recipes_with_labels = recipes.copy()
    recipes_with_labels[dataset.LABEL_COLUMN] = labels[dataset.LABEL_COLUMN]
    return recipes_with_labels


def database():
    global _DATABASE
    if _DATABASE is None:
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
def get_recipes():
    if not __is_valid_request(request.args):
        LOG.info('No class param present')
        return {'error': 'class is not present'}, 400

    recipe_class = int(request.args.get('class'))
    all_recipes = database()
    recipes_with_label = all_recipes[all_recipes[dataset.LABEL_COLUMN] == recipe_class]
    recipes_with_given_label = recipes_with_label[['id', 'name']].to_dict('records')
    if request.args.get('count'):
        number_of_recipes = int(request.args.get('count'))
        return {'data': random.sample(recipes_with_given_label, number_of_recipes)}, 200
    return {'data': recipes_with_given_label}, 200
