def number_of_words(text):
    words=text.split()
    return len(words)
def number_of_each_letter(text):
    alphabet=set()
    alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    d={}
    for letter in alphabet:
        d[letter]=0
    lowered_text=text.lower()
    for letter in lowered_text:
        if letter in alphabet:
            d[letter]+=1
    return d
def sort_on(dict):
    return dict["num"]


    
def main():
    with open ("/home/fedlix/workspace/github.com/fedriko/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankestein.txt ---")
    nb_words=number_of_words(file_contents)
    print(f"{nb_words} words found in the document")
    print("")
    dict=number_of_each_letter(file_contents)
    list=[]
    for element in dict:
        list.append({"letter":element,"num":dict[element]})
    list.sort(reverse=True,key=sort_on)
    for item in list:
        print(f"The character'{item["letter"]}' was found {item["num"]} times")
    print ("--- End repport ---")
    
   

main()

