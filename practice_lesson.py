import helpers
import display
import learn_lesson

def advance_learning_date(review_lesson):
  """Remove one int list item from the learning spacing list
  until the list is length one. At this point message should display completed."""
  if len(review_lesson[1]) != 1:
    review_lesson[1].pop()
  return review_lesson

def practice_main(unit, review):
  """Takes lesson data and review lesson list as inputs. Displays the selected unit.
  Allows user to practice the unit and set vocabulary as known or unknown,
  reduces the spacing counter, allows user to mark vocab as known or difficult
  and saves the updated data. Returns nothing."""
  display.display_lessons(review)
  user_choice = helpers.get_user_choice(ordered_list=review)
  review_lesson = display.get_lesson(review, user_choice)
  review_lesson = display.display_lesson(review_lesson)
  vocab = display.get_vocab(review_lesson)
  pause = input('Press any key to continue')
  learn_lesson.learn_lesson(vocab)
  learn_lesson.learn_lesson(vocab, kind='e')
  learn_lesson.learn_lesson(vocab, kind='s')
  helpers.set_date(review_lesson)
  review_lesson = display.display_lesson(review_lesson, marker='known')
  review_lesson = display.display_lesson(review_lesson, marker='difficult')
  review_lesson = advance_learning_date(review_lesson)
  # match lesson on title and replace updated lesson with old lesson
  for i in range(len(unit)):
    if unit[i][-1] == review_lesson[-1]:
      unit[i] = review_lesson
  helpers.write_file('lesson_data.json', unit)
