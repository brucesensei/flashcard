import datetime as dt
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

def units_for_review(unit):
  """Iterates over lessons in the unit and compares the last viewed date to
  the current date. Returns a list of all lessons that are ready for review."""
  review_lessons = []
  current_day = dt.datetime.today()
  for lesson in unit:
    if lesson[0] != 'date_visited' and len(lesson[1]) != 1:
      last_visited_str = lesson[0]
      last_visited_obj = dt.datetime.strptime(last_visited_str, '%Y-%m-%d')
      delta = current_day - last_visited_obj
      days_passed = delta.days
      practice_intervals = lesson[1]
      practice_day = practice_intervals[-1]
      if days_passed >= practice_day:
        review_lessons.append(lesson)
  return review_lessons
