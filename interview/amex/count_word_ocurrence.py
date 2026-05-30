import re

def countWord(str: str, word: str):
    caseinsensitive = str.lower()
    words = re.split(r"[\s.,]", caseinsensitive)
    words_map = {}
    
    for w in words:
        if w not in words_map:
            words_map[w] = 1
        else:
            words_map[w] = words_map[w] + 1    
    
    if word in words_map:
        return words_map[word.lower()]
    else:
        return 0

if __name__ == '__main__':
    obtained = countWord("Java is fun. Java is great.", "java") 
    expected =  2
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = countWord("Java is fun. Java is great.", "javac") 
    expected =  0
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
