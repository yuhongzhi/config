#!/usr/bin/env python

import os
import shutil
from distutils.version import LooseVersion

CELLAR_PATH = '/usr/local/Cellar'
CELLAR_BIN_PATH = '/usr/local/bin'

if __name__ == '__main__':
    module_list = os.listdir(CELLAR_PATH)
    for module in module_list:
        module_path = os.path.join(CELLAR_PATH, module)
        version_list = os.listdir(module_path)
        if len(version_list) == 1:
            continue
        last_index = len(version_list)-1
        for version in version_list[:last_index]:
            if LooseVersion(version) > LooseVersion(version_list[last_index]):
                version_path = os.path.join(module_path, version_list[last_index])
                version_list[last_index] = version
            else:
                version_path = os.path.join(module_path, version)
            shutil.rmtree(version_path)
            print("Delete " + version_path)

    #link_list = os.listdir(CELLAR_BIN_PATH)
    #for link in link_list:
    #    if not os.path.isfile(os.path.realpath(link)):
    #        print link + " --> " + os.path.realpath(link)
