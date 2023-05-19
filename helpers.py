import io
import json
import datetime as dt

def menu(title='', ordered_list=[], menu_list=[], show_ordered_list=''):
  """Takes title, ordered list(a list automacitally assigned indexes for access)
  and menu_list(a list of tuples with 0 index holding the key to press, and 1 index holing the message)
  as key-word arguments. all or none can be supplied. Returns nothing."""
  if title:
    print(f'''\n
{title.upper()}
{"=" * len(title)}\n''')   
  if ordered_list:
    if show_ordered_list:
      for i in range(len(ordered_list)):
        print(f'{i}  {ordered_list[i]}')
  if menu_list:
    for menu_item in menu_list:
      print(f'{menu_item[0]}   {menu_item[1]}')

def get_user_choice(ordered_list=[], menu_list=[]):
  """Takes the lists shown to the user and creates a list of valid choices
  to check for valid user input. Returns the user's valid choice."""
  while True:
    valid_choices = [str(i) for i in range(len(ordered_list))]
    if menu_list:
      extra_choices = [i[0] for i in menu_list]
      valid_choices.extend(extra_choices)
    user_choice = input('\nChoose an option ')
    if user_choice not in valid_choices:
      continue
    if user_choice.isnumeric():
      user_choice = int(user_choice)
    return user_choice

def tell_listen(title='', ordered_list=[], menu_list=[], message='', tell=True, show_ordered_list=True):
  """combines menu and get_user_choice into one function. Returns the user choice"""
  if tell:
    menu(title, ordered_list, menu_list, show_ordered_list) # type: ignore
  if message:
    print(message)
  return get_user_choice(ordered_list, menu_list)
  
def read_file(file):
  """Takes a file to read and returns a python data type"""
  with io.open(file, 'r', encoding='utf8') as f:
    data = f.read()
    return json.loads(data)
  
def write_file(file_name, data):
  """Takes the file to write to and the data to write to the file and writes to a json file."""
  with io.open(file_name, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=2)

def set_date(lesson):
  """takes a lesson and sets 'date_visited' to string of the current date."""
  view_date = dt.datetime.today()
  view_date_str = view_date.strftime('%Y-%m-%d')
  lesson[0] = view_date_str
