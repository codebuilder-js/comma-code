items = ['apples', 'bananas', 'tofu', 'cats']
lastIndex = len(items) - 1

def listToString(value):
  for index, item in enumerate(value):
    if index == lastIndex:
      print('and ' + item + '.')
    elif index == lastIndex - 1:
      print(item, end=' ')
    else:
      print(item, end=', ')

listToString(items)