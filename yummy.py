from io import BytesIO
import os
import random
import sys

import fabulous.image
import fabulous.utils
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_loader
import requests

from dotenv import load_dotenv
load_dotenv()

EDAMAM_ENDPOINT = "https://api.edamam.com/search"

# Hack: Fabulous has a Python 2/3 bug that keeps a width parameter from
# working.  As a workaround, make Python 2's basestring work in Python 3.
fabulous.image.basestring = str


def fetch_recipe(keywords):
    params = {
        'q': ' '.join(keywords),
        'app_id': os.getenv('EDAMAM_APP_ID'),
        'app_key': os.getenv('EDAMAM_APP_KEY'),
    }
    r = requests.get(EDAMAM_ENDPOINT, params=params)
    results = r.json()
    return random.choice(results['hits'])['recipe']


def print_recipe_text(recipe):
    print(recipe['label'])
    print('   (' + recipe['url'] + ')')
    for ingredient in recipe['ingredientLines']:
        print(' - ' + ingredient)


def print_recipe_image(recipe):
    image_url = recipe['image']
    r = requests.get(image_url)
    print(fabulous.image.Image(BytesIO(r.content), width=fabulous.utils.term.width // 3))


# Code for meta finder and loader based on https://stackoverflow.com/a/43573798/25507

class YummyMetaFinder(MetaPathFinder):
    BLACKLIST = ['nt']

    def find_spec(self, fullname, path, target=None):
        if fullname in self.BLACKLIST:
            return None
        if path is None or path == "":
            path = [os.getcwd()]  # top level import
        return spec_from_loader(fullname, loader=YummyLoader(fullname))


class YummyLoader(Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        return None  # use default module creation semantics

    def exec_module(self, module):
        print("yum, %s..." % self.filename)
        recipe = fetch_recipe(self.filename.split('_'))
        print_recipe_text(recipe)
        print_recipe_image(recipe)


def install():
    """Inserts the finder into the import machinery"""
    sys.meta_path.append(YummyMetaFinder())


install()
