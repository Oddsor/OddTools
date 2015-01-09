import pkgutil
import xml

def get_modulenames(package, show_hidden=False):
    modules = list()
    for modname in pkgutil.iter_modules(package.__path__):
        if show_hidden or not str(modname[1]).startswith('_'):
            modules.append(modname[1])
    return modules

if __name__ == '__main__':
    print(get_modulenames(xml))