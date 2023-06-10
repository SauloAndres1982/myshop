def fix_name(my_list):
    if len(my_list):
        new_list = []
        for item in my_list:
            for element in item:
                new_list = new_list.append(element)
    else:
        new_list = [element for item in my_list for element in item]

    return sorted(new_list, reverse=True)

fix_name([3,4], [2,6])