__author__ = 'Odd'

import configparser

class OddConfig():

    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()
        self.config.read(path)

config = configparser.ConfigParser()
read_files = list()
read_files.extend(config.read('settings.ini'))

if "DEFAULT" not in config:
    config.add_section("DEFAULT")


def read(path):
    read_files.extend(config.read(path))


def get_setting(key, section='DEFAULT'):
    if config.has_option(section, key):
        return config[section][key]
    else:
        raise Exception("Key " + key + " not found in config file. " + str(read_files))