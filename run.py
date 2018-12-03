from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from parsers.html import HtmlParser
from nlp.tokenizers import Tokenizer
from summarizers.lex_rank import LexRankSummarizer as lexSum
from summarizers.luhn import LuhnSummarizer as luhnSum
from summarizers.text_rank import TextRankSummarizer as textSum
from nlp.stemmers import Stemmer
from utils import get_stop_words
from tkinter import *
from summarizers.AI_Algorithm import ourSummarizer as ourSum

LANGUAGE = "english"
SENTENCES_COUNT = 10
runCount = 0
displayCount =0

if __name__ == "__main__":
   #url = "https://www.npr.org/2018/10/21/658921379/futuristic-dreams-turn-to-nightmare-in-electric-state"

   root = Tk()
   root.title("")
   #was 440, 60
   root.geometry("440x100")


   text = Text(root)
   text.tag_config("c",justify = CENTER)
   text.insert(INSERT, "Enter a URL for Summarization","c")
   text.pack()

   #was 70
   e = Entry(root, width=45)
   #was 10, 5
   e.place(x=10, y=25)

   e.focus_set()


   def display(label, parser, summarizer):
       label.delete(1.0, END)
       summarizer.stop_words = get_stop_words(LANGUAGE)


       #USED TO COUNT THE WORDS IN A SUMMARY
       global displayCount
       counter = 0
       displayCount += 1
       '''for item in summarizer(parser.document,SENTENCES_COUNT):
           for word in parser.tokenize_words(item):
               counter+=1
       print(" wordcount ", counter)
       print("--------------------")
       if displayCount%3==0:
           print("--------ARTICLE ",runCount+26,"------------")
       #END SUMMARY COUNT CODE'''


       for sentence in summarizer(parser.document, SENTENCES_COUNT):
           label.insert(END, sentence)


   def callback():
       url = e.get()
       #root.destroy()
       newWindow = Tk()
       '''#ADDED TO COUNT RUNS
       global runCount
       runCount +=1
       #END'''
       newWindow.title("Click an Algorithm to View the Summarization")
       newWindow.geometry("645x445")
       mainDisplay = Text(newWindow, wrap=WORD)
       buttonLex = Button(newWindow, text="LexRank", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), lexSum(Stemmer(LANGUAGE))))
       #was x= 260
       buttonLex.place(x=230, y=10)
       buttonLuhn = Button(newWindow, text="Luhn", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), luhnSum(Stemmer(LANGUAGE))))
       buttonLuhn.place(x=300, y=10)
       buttonText = Button(newWindow, text="TextRank", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), textSum(Stemmer(LANGUAGE))))
       buttonText.place(x=350, y=10)
       buttonPersonal = Button(newWindow, text="Ours", command=lambda: display(mainDisplay, HtmlParser.from_url(url, Tokenizer(LANGUAGE)), ourSum(Stemmer(LANGUAGE))))
       buttonPersonal.place(x=425, y=10)
       mainDisplay.place(x=0, y=50)
       newWindow.mainloop()

   b = Button(root, text="Summarize", width=40, command=callback)
   #was 68, 30
   b.place(x=40, y=65)

   mainloop()
