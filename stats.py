def count_of_words(book_text):
    words = book_text.split()
    return len(words)

def count_of_letters(book_text):
    new_book_text = book_text.lower()
    unique_characters = set(new_book_text)
    count_of_characters = {}
    for char in unique_characters:
        count_of_characters[char] = 0
    
    for char in new_book_text:
        count_of_characters[char] += 1
    
    return count_of_characters
    
def sort_on(dict):
    return dict["num"]

def sorted_letter_count(letter_and_count):
    new_list = []
    dict_letter_and_count = {}
    for char in letter_and_count:
        dict_letter_and_count["char"] = char
        dict_letter_and_count["num"] = letter_and_count[char]
        #print(dict_letter_and_count)
        new_list.append(dict(dict_letter_and_count))
    
    new_list.sort(reverse=True, key=sort_on)

    return(new_list)

