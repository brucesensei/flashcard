from time import sleep
import sys
import helpers
import choose_lesson
import create_lesson_data

def quit_app():
  print('Thank you for using your flashcard app.')
  sleep(2)
  sys.exit()

choices = {'v': choose_lesson.choose_main,
           'r': create_lesson_data.create_lesson_data,
           'q': quit_app,
           }
  
def main():
  while True:
    main_options = [
      ['v', 'view lessons'], 
      ['r','Reset module'],
      ['q', 'Quit']]
    user_choice = helpers.tell_listen(title='main menu', menu_list=main_options)
    option = choices.get(user_choice) # type: ignore
    option() # type: ignore

if __name__ == '__main__':
  main()
