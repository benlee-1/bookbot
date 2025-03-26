from stats import get_number_count, count_characters
def get_book_text(filepath: str):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main():
    returned = get_book_text("./books/frankenstein.txt")
    word_count = get_number_count(returned)
    print(f'{word_count} words found in the document') 
    dict = count_characters(returned)
    print(dict)
    
main()