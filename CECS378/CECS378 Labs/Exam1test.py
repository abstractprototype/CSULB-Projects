import string
from random import shuffle

def fillKey(phrase: str) -> str:
    phrase = phrase.lower()
    new = [i for i in string.ascii_lowercase if i not in phrase]
    shuffle(new)
    return phrase + ''.join(new)


def encryptText(text: str, key: str) -> str:
    """
        Given a key, encrypts a text using
        simple substitution
    """
    text = list(text.lower())
    map = dict(zip(key, string.ascii_lowercase))

    # Replace all letters from the key
    for i in range(len(text)):
        if text[i] not in string.ascii_lowercase:
            continue
        else:
            text[i] = map[text[i]]

    return ''.join(text)

def main():
    key = fillKey("DEARJOHNBLUY")
    print(encryptText("COMPUTER SECURITY", key))

if __name__ == "__main__":
    main()