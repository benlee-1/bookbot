def get_number_count(book:str):
    num_words = len(book.split())
    return num_words

def count_characters(book:str):
    charcter_map = dict()
    for char in book:
        lower_char = char.lower()
        if lower_char in charcter_map:
            charcter_map[lower_char] = charcter_map[lower_char]  + 1
        else:
            charcter_map[lower_char] = 1
    return charcter_map

def get_sorted_list_of_dict(dict):
    def sort_on(dict):
        return dict["count"]
    list_of_dict = []
    
    for key in dict:
        list_of_dict.append({"char": key, "count": dict[key]})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict