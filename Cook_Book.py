import pprint

cook_book = {}

with open('cook_book.txt', 'r') as f:
  
  for line in f:
    cook_book.update({line.rstrip(): []})
    ing_numb = int(f.readline())
    
    for i in range(ing_numb):
      ing_list = f.readline().rstrip()
      ing_list = ing_list.split(' | ')
      ingredient = {'ingredient_name': ing_list[0], 'quantity': ing_list[1], 'measure': ing_list[2]}
      cook_book[line.rstrip()].append(ingredient)
    
    f.readline()
    
pprint.pprint(cook_book)
print('-----------------------')

def get_shop_list_by_dishes(dishes, person_count):
  list_by_dishes = {}

  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingredient_name'] in list_by_dishes:
        temp_dish = list_by_dishes[ingredient['ingredient_name']]
        new_format = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': temp_dish['quantity'] + person_count * int(ingredient['quantity'])}}
        list_by_dishes.update(new_format)
      else:
        new_format = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': person_count * int(ingredient['quantity'])}}
        list_by_dishes.update(new_format)
  
  return list_by_dishes

dishes = ['Фахитос', 'Омлет']
person_count = 2
pprint.pprint(get_shop_list_by_dishes(dishes, person_count))
print('-----------------------')


text_to_collide = ['1.txt', '2.txt', '3.txt']
text_collider = []

def deep_dive(tuple):
  return int(tuple[1])

for text in text_to_collide:
  with open(text, 'r') as f:
    data = f.readlines()
    text_collider.append((text, len(data), data))

text_sorted = sorted(text_collider, key=deep_dive)

pprint.pprint(text_sorted)

with open('1+2+3.txt', 'w') as f:
  for text in text_sorted:
    f.write(f"{str(text[0])}\n{str(text[1])}\n")
    for line in text[2]:
      f.write(line)
    f.write("\n")