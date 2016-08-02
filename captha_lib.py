# -*- coding: utf-8 -*-
from PIL import Image
from antigate import AntiGate

from config import Conf

try:
    from logger import Logger
except ImportError:
    pass

__author__ = 'whoami'
__version__ = '1.0.0'
__date__ = '30.03.16 3:38'
__description__ = """
Description for the python module
"""

try:
    logger = Logger()
except NameError:
    logger = None


class RecognizeCaptcha(AntiGate):
    captcha_file = 'captcha.png'

    def __init__(self):
        self.conf = Conf()
        self.conf.read_section('antigate')

        super().__init__(auto_run=False, **self.conf.namespace)

    def crop_image(self, image_path, captcha_size):
        image = Image.open(image_path)
        image.crop(captcha_size).save(self.captcha_file)

    def _balance(self):
        balanse = super().balance()
        if logger:
            logger.info("Balance: {}".format(balanse))
        if balanse < 1:
            raise RuntimeWarning('Out of balance!!!')

    def recognize(self, image: str, rect: 'element rect'):
        try:
            self.balance()
        except RuntimeWarning:
            return None

        captcha_size = (rect['x'],
                        rect['y'],
                        rect['width'] + rect['x'] - 1,
                        rect['height'] + rect['y'] - 1)

        self.crop_image(image, captcha_size)
        super().run(self.captcha_file)

