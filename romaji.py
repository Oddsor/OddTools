import requests
import re

def get_romaji(word):
    '''
    >>> get_romaji('進撃の巨人')
    'shingeki no kyojin'

    :param word:
    :return:
    '''
    r = requests.get('http://www.romajidesu.com/translator/' + word)
    content = r.text
    r.close()
    frontsplit = re.sub('.*<div id="res_romaji">.*?<span.*?>',
                        '', content, flags=re.DOTALL)
    backsplit = re.sub('</span>\s*</div>.*<div id="res_kana".*',
                       '', frontsplit, flags=re.DOTALL)
    split = re.sub('</span>\s*?<span.*?>', ' ', backsplit,
                   flags=re.DOTALL)
    return split

import unittest


class TestRomajiTranslation(unittest.TestCase):
    def test_attackontitan(self):
        self.assertEqual(get_romaji('進撃の巨人'), 'shingeki no kyojin')

if __name__ == '__main__':
    pass