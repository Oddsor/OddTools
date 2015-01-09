import pkgutil
import xml

def get_modules():
    for modname in pkgutil.iter_modules(xml.__path__):
        print(modname)

if __name__ == '__main__':
    get_modules()