import nltk
from resume.lists.education import RESERVED_WORDS

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_education(input_text):
  organizations = []
  reserved_words_lower = list(map(lambda x: x.lower(), RESERVED_WORDS))

  for sent in nltk.sent_tokenize(input_text):
    # print("sent")
    # print(sent)
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      # if hasattr(chunk, 'label'):
      #   print("chunk")
      #   print(chunk)
      #   print(chunk.label())
      if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
        organizations.append(' '.join(c[0] for c in chunk.leaves()))

  education = set()
  for org in organizations:
    for word in reserved_words_lower:
      if org.lower().find(word) >= 0:
        education.add(org)
 
  return education