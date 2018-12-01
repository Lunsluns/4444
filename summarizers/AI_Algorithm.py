from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from ._summirizer import AbstractSummarizer
#from stop_words import get_stop_words
import sys
sys.path.append('..')
from models.tf import TfDocumentModel

class JackieSummarizer(AbstractSummarizer):
    max_gap_size = 4 #these are unusued
    significant_percentage = 1 #unused
    _stop_words = frozenset()

    @property
    def stop_words(self):
        return self._stop_words

    @stop_words.setter
    def stop_words(self, words):
        self._stop_words = frozenset(map(self.normalize_word, words))

    def __call__(self, document, sentences_count):
        words = self._get_significant_words(document.words)
        word_ratings = self._get_word_ratings(words)
        sentence_ratings = self._get_sentence_ratings(document.sentences, word_ratings)

        return self._get_summary(document.sentences, sentences_count, sentence_ratings)

    def _get_significant_words(self, words):
        word_list = map(self.normalize_word, words)
        word_list = tuple(self.stem_word(w) for w in word_list if w not in self._stop_words)
        #print(word_list)
        model = TfDocumentModel(word_list)

        # take only words that occur more than once and are significant (not stop words)
        best_words_count = int(len(word_list) * self.significant_percentage)
        word_list = model.most_frequent_terms(best_words_count)
        word_list = list(t for t in word_list if model.term_frequency(t) > 1)

        word_amounts = {}

        #get the amount of times every word occurs, put words as keys to the amount of times they occur
        for word in word_list:
            word_amounts[word] = model.term_frequency(word)

        return word_amounts

    def _get_word_ratings(self, words):
        # rate words by seperately dividing the amount that they occur by the amount of each other word, and then summing the results
        # ex: word1amount/word2amount + word1amount/word3amount + word1amount/word4amount + ...
        # no point in using frequency instead of amount b/c denominator would get divided out
        word_rating = {}
        for word, word_amount in words.items():
            word_rating[word] = 0
            for comparator, comp_amount in words.items():
                word_rating[word] = int(word_rating[word]) + (word_amount/comp_amount)

        return(word_rating)

    def _get_sentence_ratings(self, sentences, words):
        #add all the word ratings in each sentence to get the sentence ratings
        sentence_rating = []
        i = 0
        for sentence in sentences:
            sentence_rating.append(0)
            for order, word in enumerate(sentence.words):
                key = self.normalize_word(word)
                key = self.stem_word(key)
                if key in words:
                    sentence_rating[i] = int(sentence_rating[i] + words[key])
            i += 1
        return(sentence_rating)

    def _get_summary(self, sentences, sentences_count, sentences_ratings):
        summary = []
        top_sentences = []
        top_sentences_ratings = []
        #find the 10 highest rated sentences and record where they occur in the document
        for i in range (0,10):
            top_sentences_ratings.append(0)
            for j in range (0, len(sentences_ratings)):
                if sentences_ratings[j] > top_sentences_ratings[i]:
                    top_sentences_ratings[i] = sentences_ratings[j]
                    current_top = j
            sentences_ratings[current_top] = 0
            top_sentences.append(current_top)

        next_sentence = len(sentences_ratings)
        to_eliminate = 0

        #print the 10 highest rated sentences in order of where they occur in the document
        for i in range (0,10):
            for i in range(0, len(top_sentences)):
                if top_sentences[i] < next_sentence:
                    next_sentence = top_sentences[i]
                    to_eliminate = i
            summary.append(str(sentences[next_sentence]))
            del top_sentences[to_eliminate]
            next_sentence = len(sentences_ratings)
        #print(summary)
        return summary
