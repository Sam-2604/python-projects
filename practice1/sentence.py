# Ask the user for a sentence, output a dictionary where each unique word is a key and 
# its value is how many times it appeared — sorted alphabetically, case insensitive. 
# Then print only words that appeared more than once.

def main():
    words= {}
    sentence = input("Enter a sentence: ")
    sentence = sentence.lower()
    words_list = sentence.split()

    for word in words_list:
        words[word] = words.get(word, 0) + 1
        
    for word, count in sorted(words.items()):
        if count >= 1:
            print(f"{word}: {count}")
        
    for word, count in sorted(words.items()):    
        if count > 1:
            print(f"{word}")

main()