'''  HASHCODE 2022
Team Name :- MasterMind4
Team member Linkedin:-
        1) https://www.linkedin.com/in/tanmay-bhale-5361b8228/ 
        2) https://www.linkedin.com/in/harshal-bodhe-41b80420b/
        3) https://www.linkedin.com/in/ayush-kumar-namdeo-3aa198194/
        4)

github repo :- https://github.com/ayushnamdeo02/MasterMind4-hashcode2022
'''

#Solution 

## create dict
ingredient_dict = dict()

## reading data
with open('./input_data/a_an_example.in.txt') as file:
    #seprating the line number in id and rest line in line
    for id, line in enumerate(file.readlines()):    
        data = line.strip() ## strip newline
        items_list = str(data).split() ## create list
        if id > 0: ## start with clients
            if id % 2 == 1: ## like
                del items_list[0]
                for i in items_list:
                    if i not in ingredient_dict.keys():
                        ingredient_dict[i] = 1
                    else:
                        ingredient_dict[i] += 1

            elif id == 0:
                pass

            else: # dislike
                del items_list[0]
                for i in items_list:
                    if i not in ingredient_dict.keys():
                        ingredient_dict[i] = 0
                    else:
                        ingredient_dict[i] -= 1

## create output
final_ingredient = set()

cnt = 0
for k, v in ingredient_dict.items():
    if v > 0:
        final_ingredient.add(k)
        cnt += 1

## create string
ingredients = ' '.join(list(final_ingredient))
output_string = str(cnt) + ' ' + ingredients

with open('./output/a_an_example.out.txt', 'w') as file:
    file.write(output_string)