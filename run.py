# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from parsers.html import HtmlParser
#from parsers.plaintext import PlaintextParser
from nlp.tokenizers import Tokenizer
from summarizers.lex_rank import LexRankSummarizer as lexSum
from summarizers.luhn import LuhnSummarizer as luhnSum
from summarizers.text_rank import TextRankSummarizer as textSum
from nlp.stemmers import Stemmer
from utils import get_stop_words

from tkinter import *


LANGUAGE = "english"
SENTENCES_COUNT = 10


if __name__ == "__main__":
    #url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    url = "https://www.npr.org/2018/10/21/658921379/futuristic-dreams-turn-to-nightmare-in-electric-state"

    root = Tk()
    e = Entry(root)
    e.pack()

    e.focus_set()

    def display(label, parser, summarizer):
        label.delete(1.0, END)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            label.insert(END, sentence)

    def callback():
        url = e.get()
        newWindow = Tk()
        mainDisplay = Text(newWindow)
        mainDisplay.pack()
        buttonLex = Button(newWindow, text="Lex", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), lexSum(Stemmer(LANGUAGE))))
        buttonLex.pack()
        buttonLuhn = Button(newWindow, text="Luhn", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), luhnSum(Stemmer(LANGUAGE))))
        buttonLuhn.pack()
        buttonText = Button(newWindow, text="Text", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), textSum(Stemmer(LANGUAGE))))
        buttonText.pack()
        newWindow.mainloop()

    b = Button(root, text="Summarize", width=40, command=callback)
    b.pack()

    mainloop()