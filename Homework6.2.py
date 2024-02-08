my_dict_1 = {1:1, 2:2, 3:3}
my_dict_2 = {2:22, 4:44, 5:55}
merged_dict = {k:[my_dict_1.get(k), my_dict_2.get(k)] if k in my_dict_1 and k in my_dict_2 else my_dict_1.get(k) or my_dict_2.get(k) for k in set(my_dict_1.keys()).union(set(my_dict_2.keys()))}
print(merged_dict) # {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}