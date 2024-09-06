class SortByAge:
    def __call__(self, list_of_tuples):
        # Defining a function to get the age from a tuple
        def get_age(person_tuple):
            return person_tuple[1]
        # Sort the list of tuples by age (using get_age function)
        return sorted(list_of_tuples, key=get_age)

sort_by_age = SortByAge()

people = [("Lucy", 30), ("Danny", 25), ("Peter", 35), ("Joshua", 50)]
sorted_people = sort_by_age(people)  # sort the list by age 

print("Sorted list by age:", sorted_people)