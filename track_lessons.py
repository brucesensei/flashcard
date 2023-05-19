import display


def get_difficult_words(unit):
  """Returns a list of all words marked as difficult."""
  difficult_words = []
  for lesson in unit:
    vocab = display.get_vocab(lesson)
    for word in vocab:
      if word['difficult'] == True:
        difficult_words.append(word)
  return difficult_words

def get_known_word_count(unit):
  """Checks for vidited lessons in the unit and returns (int) the total number of
  words in all the visited lessons."""
  total = 0 
  for lesson in unit:
    if lesson[0] != 'date_visited':
      word_count = len(lesson[2:-1])
      total += word_count  
  return total

def units_for_review():
  # returns lessons up for review by time stamp information.
  return 0