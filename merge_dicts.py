class MergeDicts:
    def __call__(self, dict1, dict2):
        # Creating a dictionary to hold the merged result
        merged_dict = dict1.copy() 

        for key, value in dict2.items():
            if key in merged_dict:    # if the key already there sum it up to the existing
                merged_dict[key] += value
            else:                     # if the key is new add it to the merge dictioanry 
                merged_dict[key] = value

        return merged_dict
    
merge_dicts = MergeDicts()

dict1 = {"Book": 4, "Paint brush": 3}
dict2 = {"Paint brush": 1, "Pen": 5}

result = merge_dicts(dict1, dict2)

print("Merged dictionary:", result)