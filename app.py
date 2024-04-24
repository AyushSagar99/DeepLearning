
import gc
from summa import summarizer
import streamlit as st

# from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation   
# import heapq
# import sumy
import nltk
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')
def lsa_summary(text, no_sentences, lang):
    parser = PlaintextParser.from_string(text, Tokenizer(lang))
    lsa_sum = LsaSummarizer()
    summary = lsa_sum(parser.document, no_sentences)
    gc.collect()
    return [str(sentence) for sentence in summary]
# def summarize(text, per):
#     nlp = spacy.load('en_core_web_sm')
#     doc= nlp(text)
#     tokens=[token.text for token in doc]
#     word_frequencies={}
#     for word in doc:
#         if word.text.lower() not in list(STOP_WORDS):
#             if word.text.lower() not in punctuation:
#                 if word.text not in word_frequencies.keys():
#                     word_frequencies[word.text] = 1
#                 else:
#                     word_frequencies[word.text] += 1
#     max_frequency=max(word_frequencies.values())
#     for word in word_frequencies.keys():
#         word_frequencies[word]=word_frequencies[word]/max_frequency
#     sentence_tokens= [sent for sent in doc.sents]
#     sentence_scores = {}
#     for sent in sentence_tokens:
#         for word in sent:
#             if word.text.lower() in word_frequencies.keys():
#                 if sent not in sentence_scores.keys():                            
#                     sentence_scores[sent]=word_frequencies[word.text.lower()]
#                 else:
#                     sentence_scores[sent]+=word_frequencies[word.text.lower()]
#     select_length=int(len(sentence_tokens)*per)
#     summary=heapq.nlargest(select_length, sentence_scores,key=sentence_scores.get)
#     final_summary=[word.text for word in summary]
#     summary=''.join(final_summary)
#     print(final_summary,"hmmmm")
#     print(summary,"hmmmmrwertyuil")
#     return final_summary

# Add title on the page
st.title("Text summarization")

# Ask user for input text
input_sent = st.text_area("Input Text", "This is a test summary", height=400)

ratio = st.slider(
    "Summarization fraction", min_value=1, max_value=100, value=1, step=1
)

# Display named entities
summarized_text = lsa_summary(input_sent, ratio, "english")

print("sdfghjklk;jlhgfc",summarized_text)
for sentence in summarized_text:
    print(sentence,"Jdksflsj")
    st.write(sentence)