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
    #url = "https://www.npr.org/2018/10/21/658921379/futuristic-dreams-turn-to-nightmare-in-electric-state"

    root = Tk()
    root.geometry("440x60")
    e = Entry(root, width=70)
    e.place(x=10, y=5)

    e.focus_set()

    def display(label, parser, summarizer):
        label.delete(1.0, END)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            label.insert(END, sentence)

    def callback():
        url = e.get()
        newWindow = Tk()
        newWindow.geometry("645x445")
        mainDisplay = Text(newWindow, wrap=WORD)
        buttonLex = Button(newWindow, text="Lex", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), lexSum(Stemmer(LANGUAGE))))
        buttonLex.place(x=260, y=10)
        buttonLuhn = Button(newWindow, text="Luhn", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), luhnSum(Stemmer(LANGUAGE))))
        buttonLuhn.place(x=300, y=10)
        buttonText = Button(newWindow, text="Text", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), textSum(Stemmer(LANGUAGE))))
        buttonText.place(x=350, y=10)
        mainDisplay.place(x=0, y=50)
        newWindow.mainloop()

    b = Button(root, text="Summarize", width=40, command=callback)
    b.place(x=68, y=30)

    mainloop()