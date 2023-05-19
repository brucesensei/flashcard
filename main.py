from time import sleep
import sys
import helpers
import choose_lesson

def quit_app():
  print('Thank you for using your flashcard app.')
  sleep(2)
  sys.exit()

choices = {'l': choose_lesson.choose_main,
           'v': "archive.view_archive",
           's': "archive.archive_lesson",
           'r': "archive.restore_lesson",
           'a': "add_native.main",
           'd': "delete_native.mian",
           'q': quit_app,
           }
  
def main():
  while True:
    main_options = [
      ['l', 'view lessons'], 
      ['v','View archive'], 
      ['s', 'Store a lesson'], 
      ['r', 'Restore a lesson'],
      ['a', 'Add a lesson'],
      ['d', 'Delete a lesson'],
      ['q', 'Quit']]
    user_choice = helpers.tell_listen(title='main menu', menu_list=main_options)
    option = choices.get(user_choice) # type: ignore
    option() # type: ignore

if __name__ == '__main__':
  main()
