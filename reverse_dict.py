dict1={'bar':'foo', 'spam':'eggs','bazz':'foo', 'ggg':'foo'}
new_dict={}

for key,val in dict1.items():
    if val not in new_dict:
        new_dict[val]=[key]
    else:
        new_dict[val].append(key)
print(new_dict)