frankenstein_path = "books/frankenstein.txt"

def main():
    
    file_contents = get_book_text(frankenstein_path)
    #print(file_contents)

    counter = get_word_count(file_contents)
    #print(counter)

    letter_count = get_letter_count(file_contents)
    #print(letter_count)

    #report
    book_report(file_contents, frankenstein_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_dic ={}
    for letter in text:
        lowered = letter.lower()
        if(lowered in letter_dic):
            letter_dic[lowered] += 1
        else:
            letter_dic[lowered] = 1

    return letter_dic

def sort_on(dict):
    return dict["num"]

def book_report(text, path):
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(text)} words found in the document")
    print()
    letter_dic = get_letter_count(text)
    #print(letter_dic)
    letter_list = []
    for ch in letter_dic:
        letter_list.append({"char": ch, "num": letter_dic[ch]})
        #print(ch)
    letter_list.sort(reverse=True, key=sort_on)
    
    for i in letter_list:
        if i["char"].isalpha() == True:
            print(f"The {i["char"]} character was found {i["num"]} times")

    print("--- End report ---")
    pass

main()
