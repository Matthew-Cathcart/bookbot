from stats import count_of_words, count_of_letters, sorted_letter_count
import sys 


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = count_of_words(book_text)
    letter_count = count_of_letters(book_text)
    sorted_letters = sorted_letter_count(letter_count)

    print_stats(book_path, word_count, sorted_letters)
    

def print_stats(book_path, word_count, sorted_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print((f"Found {word_count} total words"))
    print("--------- Character Count -------")
    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open (path_to_file) as f:
        return f.read()




main()