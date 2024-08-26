def main():
    get_book_path = ("books/frankenstein.txt")
    text = get_text(get_book_path) 
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars = char_func(text)
    print(chars)
    char_sorted_list = chars_dict_to_sorted_list(chars)

    print(f"--- Begin report of {get_book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(nums_chars_dict):
    sorted_list = []
    for ch in nums_chars_dict:
        sorted_list.append({"char":ch, "num": nums_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_text(get_book_path):
    with open(get_book_path) as f:
        return f.read()
    
def char_func(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    return char_dict




        
    

    
def get_num_words(text):
    words = text.split()
    return len(words)



main()