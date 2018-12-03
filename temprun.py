from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from parsers.html import HtmlParser
#from parsers.plaintext import PlaintextParser
from nlp.tokenizers import Tokenizer
from summarizers.lex_rank import LexRankSummarizer as lexSum
from summarizers.luhn import LuhnSummarizer as luhnSum
from summarizers.text_rank import TextRankSummarizer as textSumi
from summarizers.AI_Algorithm import ourSummarizer as ourSum
from nlp.stemmers import Stemmer
from utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 10


#A temporary script to run our summarizer for the time bieng

if __name__ == "__main__":

    url = "https://www.livescience.com/64184-mini-placentas-lab-grown.html"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = ourSum(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)

    counter = 0
    for item in summarizer(parser.document, SENTENCES_COUNT):
        for word in parser.tokenize_words(item):
            counter += 1
    print("")
    print(" wordcount ", counter)
