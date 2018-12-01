from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from parser.html import HtmlParser
#from parsers.plaintext import PlaintextParser
from nlp.tokenizers import Tokenizer
from summarizers.lex_rank import LexRankSummarizer as lexSum
from summarizers.luhn import LuhnSummarizer as luhnSum
from summarizers.text_rank import TextRankSummarizer as textSumi
from summarizers.Jackie import JackieSummarizer as jackieSum
from nlp.stemmers import Stemmer
from utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 10


#A temporary script to run Jackie's summarizer for the time bieng

if __name__ == "__main__":

    url = "https://www.cnn.com/2018/11/27/us/north-carolina-missing-teen-search-body-found/index.html"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = jackieSum(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)
