def translate_sentence(sentence, dictionary):
    words = sentence.split()
    translated_words = []
    for word in words:
        translated_words.append(dictionary[word])
    return " ".join(translated_words)

if __name__ == "__main__":
    N = int(input())
    sentence = input()
    M = int(input())

    dictionary = {}
    for _ in range(M):
        swedish, english = input().split()
        dictionary[swedish] = english

    translated_sentence = translate_sentence(sentence, dictionary)
    print(translated_sentence)
