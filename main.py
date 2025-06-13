from stats import text_to_String, count_char, chars_dict_to_sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    
    word_count = text_to_String(text)
    
    char_counts = count_char(text)
    
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    print(sys.argv)


main()