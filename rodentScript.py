file = open('rodents.csv')
for line in file:
    tag_id, weight = line.split(',')
    if tag_id not in rodents:
        rodents[tag_id] = Rodent(tag_id)
        rodents[tag_id].add_weight(weight)
    else:
        rodents[tag_id].add_weight(weight)
        
file.close()
