from stats import get_number_count, count_characters, get_sorted_list_of_dict
import sys
def get_book_text(filepath: str):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main():
    if len(sys.argv) == 2:
        bookpath = sys.argv[1]
        print('============ BOOKBOT ============', '\n',f'Analyzing book found at {bookpath}...')
        returned = get_book_text(f'{bookpath}')
    
        word_count = get_number_count(returned)
        print('----------- Word Count ----------', '\n', f'Found {word_count} total words')
        dict = count_characters(returned)
        sorted_list = get_sorted_list_of_dict(dict)
        print('--------- Character Count -------')
        for element in sorted_list:
            if element["char"].isalpha():
                print(f'{element["char"]}: {element["count"]}')
    else: 
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
main()