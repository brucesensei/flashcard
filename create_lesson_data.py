import helpers
import uuid

message = '''
=======================================================
|                                                     |
| \    /\    /  /\   |``\  |\  |  ``|`` |\  |  /``\   |
|  \  /  \  /  /__\  |../  | \ |    |   | \ | |   --- |
|   \/    \/  /    \ | \   |  \|  ..|.. |  \|  \../   |
=======================================================

Resetting the module will erase any recorded progress
and delete any lessons you have added. If you are sure
you want to proceed enter 'y' (yes). Otherwise press
any other key to return to the main menu.
'''
def divide_list(long_list, lesson_length):
  """splits one long list of single words into many smaller lists determined by lensson_lenght
  words each passed to the function with lesson_length."""
  length = len(long_list)
  increment = (length // lesson_length)
  remainder = length - (increment * lesson_length)
  if remainder:
    increment +=1
  unit = []
  start_index = 0
  end_index = lesson_length
  for j in range(increment):
    lesson = []
    for i in range(start_index, end_index):
      lesson.append(long_list[i])
    start_index += lesson_length
    end_index += lesson_length
    if end_index > length:
      end_index = length
    unit.append(lesson)
  return unit

def lesson_generator(target, native):
  """takes a list of target and native language pairs and creates a lesson of the word
  pairs contining the number of words in the supplied lists."""
  lesson = ["date_visited", [21, 14, 7, 3, 1]]
  if len(native) != len(target):
    print('the language lists are not the same length. please check your data and try again.')
    return
   
  for i in range(len(native)):
    id = uuid.uuid4()
    id = str(id)
    dic = {
      'id': id,
      "target": target[i],
      "native": native[i],
      "known": False,
      "difficult": False
    }
    lesson.append(dic)
  return lesson

def create_unit(target, native):
  """Takes target and native lists as inputs and passes the list items
  to lesson_generator. appends the output to a lesson and generates
  a title and appends it to the lesson. returns the lesson as a list."""
  unit = []
  for i in range(len(target)):
    title = 'Lesson ' + str(i) 
    lesson = lesson_generator(target[i], native[i])
    lesson.append(title) # type: ignore
    unit.append(lesson)
  return unit
 
def create_lesson_data():
  # get the master english and spanish word lists
  spanish_words = helpers.read_file('orriginal_spanish_list.json')
  english_words = helpers.read_file('orriginal_english_list.json')  
  # divide the word list into a list of 10-word lessons
  english_lessons = divide_list(english_words, 10)
  spanish_lessons = divide_list(spanish_words, 10)
  # create a unit containing all the lessons
  unit = create_unit(spanish_lessons, english_lessons)
  # write the data to file
  helpers.write_file('lesson_data.json', unit)
  print('All learning tracking has been reset and any added lessons have been lost.')

def confirm_reset():
  """Confirms if the user really wants to reset the lesson before allowing reset.""" 
  answer = input(message)
  if answer == 'y':
    create_lesson_data()
