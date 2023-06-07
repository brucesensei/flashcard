from time import sleep
import sys
import helpers
import choose_lesson
import create_lesson_data
import add_lesson
import store_lesson
import view_stored


def quit_app():
  print('Thank you for using your flashcard app.')
  sleep(2)
  sys.exit()
 
choices = {'v': choose_lesson.choose_main,
           'a': add_lesson.add_main,
           's': store_lesson.store_main,
           'l': view_stored.view_stored_main,
           'r': create_lesson_data.confirm_reset,
           'q': quit_app,
           }
  
def main():
  while True:
    main_options = [
      ['v', 'View lessons'], 
      ['a', 'Add lesson'],
      ['s', 'Store lesson'],
      ['l', 'View stored lessons'],
      ['r', 'Reset module'],
      ['q', 'Quit'],
      ]
    user_choice = helpers.tell_listen(title='main menu', menu_list=main_options)
    option = choices.get(user_choice) # type: ignore
    option() # type: ignore

if __name__ == '__main__':
  main()
