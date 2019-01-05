import sys
import os.path

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_loader

# Code based on https://stackoverflow.com/a/43573798/25507

class YummyMetaFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if path is None or path == "":
            path = [os.getcwd()] # top level import --
        return spec_from_loader(fullname, loader=YummyLoader(fullname))

class YummyLoader(Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        return None # use default module creation semantics

    def exec_module(self, module):
        print("yum, %s..." % self.filename)

def install():
    """Inserts the finder into the import machinery"""
    sys.meta_path.append(YummyMetaFinder())

install()

import fabulous
import bacon

