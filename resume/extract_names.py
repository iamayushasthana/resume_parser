# import nltk
 
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# def extract_names(txt):
#   names = []
#   for sent in nltk.sent_tokenize(txt):
#     for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#       if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
#         names.append(
#           ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
#         )
#   return names

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_lg')
matcher = Matcher(nlp.vocab)

def extract_names(resume_text):
  nlp_text = nlp(resume_text)

  patterns = [
    [{'POS': 'PROPN'}],
    [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
  ]

  matcher.add('NAME', patterns)
  matches = matcher(nlp_text)

  for match_id, start, end in matches:
    span = nlp_text[start:end]
    return span.text
