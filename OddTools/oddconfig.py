__author__ = 'Odd'

import configparser

class OddConfig():

    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()
        self.config.read(path)

config = configparser.ConfigParser()
config.read('settings.ini')

if "DEFAULT" not in config:
    config.add_section("DEFAULT")

def read(path):
    config.read(path)

def get_setting(key, section='DEFAULT'):
    if config.has_option(section, key):
        return config[section][key]
    else:
        raise Exception("Key " + key + " not found in config file.")


def set_setting(key, value, section='DEFAULT'):
    if not config.has_section(section):
        config.add_section(section)
    config[section][key] = value
    config.write(open("settings.ini", 'w'))