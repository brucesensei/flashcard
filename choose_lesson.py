import helpers
import learn_lesson
import display
import track_lessons
import difficult_words
import practice_lesson
 
def choose_main():
  while True:
    # read the lesson data into the function
    unit = helpers.read_file('lesson_data.json')
    # display the names of all the lessons and show learning or complete message
    display.display_lessons(unit)
    # get the word count from all the units being learned
    known_words = track_lessons.get_known_word_count(unit)
    # get a list of all the vocab words that are marked as difficult and use
    # the list length to display the number of difficult words
    difficult =  track_lessons.get_difficult_words(unit)
    # get the lessons that are scheduled for review
    review = track_lessons.units_for_review(unit)
    print(f'\nKnown Words: ({known_words})')
    menu_options = [
      ['p', f'Lessons for Review:   ({len(review)})'], # type: ignore
      ['d', f'Difficult Words       ({len(difficult)})'],
      ['r', 'Return to the main menu'],
      ]
    message = 'To learn a new lesson (enter a lesson number)'
    # get the user choice and handle routing.
    user_choice = helpers.tell_listen(title='lesson menu',
      ordered_list=unit,
      menu_list=menu_options,
      message=message,
      show_ordered_list=False
      )
    if type(user_choice) == int:
      learn_lesson.learn_main(unit, user_choice)
      continue
    if user_choice == 'd':
      if len(difficult) == 0:
        print('You do not have any difficult words to practice.')
        continue
      difficult_words.difficult_main(unit, difficult)
      continue
    if user_choice == 'p':
      if len(review) == 0: # type: ignore
        print('You do not have any lessons to review.')
        continue
      practice_lesson.practice_main(unit, review)
      continue
    if user_choice == 'r':
      break   
