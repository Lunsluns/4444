
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from itertools import chain
import sys
sys.path.append('...')
from _compat import unicode_compatible
from utils import cached_property
#sys.path.append('.')
from ._sentence import Sentence

#this file handles sentences, headings and words, it defines the paragraph object
@unicode_compatible
class Paragraph(object):
    __slots__ = (
        "_sentences",
        "_cached_property_sentences",
        "_cached_property_headings",
        "_cached_property_words",
    )

    def __init__(self, sentences):
        sentences = tuple(sentences)
        for sentence in sentences:
            if not isinstance(sentence, Sentence):
                raise TypeError("Only instances of class 'Sentence' are allowed!")

        self._sentences = sentences

    @cached_property
    def sentences(self):
        return tuple(s for s in self._sentences if not s.is_heading)

    @cached_property
    def headings(self):
        return tuple(s for s in self._sentences if s.is_heading)

    @cached_property
    def words(self):
        return tuple(chain(*(s.words for s in self._sentences)))

    def __unicode__(self):
        return "<Paragraph with %d headings & %d sentences>" % (
            len(self.headings),
            len(self.sentences),
        )

    def __repr__(self):
        return self.__str__()