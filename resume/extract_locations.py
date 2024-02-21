import nltk
from resume.lists.locations import LOCATIONS

nltk.download('stopwords')

def extract_locations(input_text):
  stop_words = set(nltk.corpus.stopwords.words('english'))
  word_tokens = nltk.tokenize.word_tokenize(input_text)

  skills_list = list(map(lambda x: x.lower(), LOCATIONS))

  filtered_tokens = [w for w in word_tokens if w not in stop_words]
  filtered_tokens = [w for w in word_tokens if w.isalpha()]
  bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
  found_locations = set()

  for token in filtered_tokens:
    if token.lower() in skills_list:
      found_locations.add(token)

  for ngram in bigrams_trigrams:
    if ngram.lower() in skills_list:
      found_locations.add(ngram)
 
  return found_locations