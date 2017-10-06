
def unique_houses(filename):
    """TODO: Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> unique_houses("cohort_data.txt")
    set(['Gryffindor', 'Hufflepuff', "Dumbledore's Army", 'Ravenclaw', 'Slytherin'])

    """

    
    #house_names = ['Gryffindor', 'Hufflepuff', "Dumbledore's Army", 'Ravenclaw', 'Slytherin']
    #items_set = ([])
    items_list = []
    file_open = open(filename)
    # for line in file_open:
    #     items = line.split('|')
    #     print items          
    #     items_list.append(items)
        # Code goes here

    items_list = [line.split('|') for line in file_open]
    # for word in items_list if
    print items_list

    houses_list = []
    for item in items_list:
        if item[2] != '':
            houses_list.append(item[2])
    # houses_list = []
    houses_list = [item[2] for item in items_list if item[2] != '']

    print "\nThe list of houses is:\n"

    print houses_list

    houses = set(houses_list)
    print "\nThe set of unique houses is:"
    print houses

if __name__ == '__main__':
    unique_houses('cohort_data.txt')