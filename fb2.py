#-*-coding:utf8-*-
from lxml import etree


class PyFb2(object):
    def __init__(self, fpath):
        self.file = fpath
        self._tree = None
        self._ns = None

    def parse(self):
        pass

    def get_title(self):
        pass

    def _get_tree(self):
        if not self._tree:
            parser = etree.XMLParser(ns_clean=True, recover=True)
            self._tree = etree.parse(self.file, parser)
        return self._tree

    def get_namespaces(self):
        if self._ns is None:
            tree = self._get_tree()
            self._ns = tree.getroot.nsmap
        return self._ns
