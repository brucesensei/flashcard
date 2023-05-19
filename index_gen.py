def question_indexes_practice(vocab):
  """Takes a list of vocab and returns a list if integers to access the questions
  from the questions dictionary"""
  length = len(vocab)
  if length == 1:
    return [0,1,2,3,4]
  half = length // 2
  first_key = 0
  second_key = 1
  indexes = []
  for i in range(2):
    for i in range(half):
      indexes.append(first_key)
      indexes.append(first_key)
      indexes.append(second_key)
      indexes.append(second_key)
    if length % 2 != 0:
      indexes.append(first_key)
      indexes.append(second_key)      
    first_key += 2
    second_key += 2
  last = [4 for i in range(length)]
  indexes.extend(last)
  return indexes

def get_half(number):
  """Helper function on vocab_indexes function. used to generate the first and second part
  of the integer list."""
  half = number // 2 
  my_list = []
  first_key = 0
  second_key = 1
  for i in range(half):
    my_list.append(first_key)
    my_list.append(second_key)
    my_list.append(first_key)
    my_list.append(second_key)
    first_key +=2
    second_key += 2
  if number % 2 != 0:
    my_list.append(number - 1)
    my_list.append(number - 1)        
  return my_list

def vocab_indexes_practice(vocab):
  """Takes a vocab list and returns a list of integers used to access the vocabulary"""
  length = len(vocab)
  vocab_indexes = []
  if length == 1:
    return [0,0,0,0,0]
  part_1 = get_half(length)
  vocab_indexes.extend(part_1)
  part_2 = get_half(length)
  vocab_indexes.extend(part_2)
  part_3 = [i for i in range(length)]
  vocab_indexes.extend(part_3)
  return vocab_indexes