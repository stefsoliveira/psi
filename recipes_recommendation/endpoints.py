# coding=utf-8
import logging
import threading

from flask import Flask

LOG = logging.getLogger(__name__)
APP = Flask(__name__)

_DATABASE = None
_DATABASE_LOCK = threading.RLock()


def _load_database():
    pass


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
