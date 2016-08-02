# -*- coding: utf-8 -*-


class DefaultConf:
    load_timeout = '60'
    implicitly_wait = '5'
    br_heigth = '550'
    br_width = '1024'
    explicit_waits = '15'
    service_args = list()
    phantomjs = 'phantomjs'
    firefox = 'firefox'
    web_driver = firefox
    test_url = 'http://whoer.net'
    screen_dir = ''

    def read_section(self, *args, **kwargs):
        pass


class DefaultLogger:
    def info(self, *args, **kwargs):
        pass

    def error(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def critical(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass