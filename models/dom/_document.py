from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from itertools import chain
import sys
sys.path.append('...')
from utils import cached_property
from _compat import unicode_compatible

#this file handles document/DOM functions, such as returning and helping to interpret paragraphs, sentences, headings, words etc.
@unicode_compatible
class ObjectDocumentModel(object):
    def __init__(self, paragraphs):
        self._paragraphs = tuple(paragraphs)

    @property
    def paragraphs(self):
        return self._paragraphs

    @cached_property
    def sentences(self):
        sentences = (p.sentences for p in self._paragraphs)
        return tuple(chain(*sentences))

    @cached_property
    def headings(self):
        headings = (p.headings for p in self._paragraphs)
        return tuple(chain(*headings))

    @cached_property
    def words(self):
        words = (p.words for p in self._paragraphs)
        return tuple(chain(*words))

    def __unicode__(self):
        return "<DOM with %d paragraphs>" % len(self.paragraphs)

    def __repr__(self):
        return self.__str__()