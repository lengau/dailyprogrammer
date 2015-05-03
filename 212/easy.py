#!/usr/bin/env python3
# Daily Programmer #212, easy edition: Rövarspråket
# http://redd.it/341c03


CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def encode(plaintext):
    """Encode text as Rövarspråket.

    Example inputs:

    >>> encode('Jag talar Rövarspråket!')
    'Jojagog totalolaror Rorövovarorsospoproråkoketot!'
    >>> encode("I'm speaking Robber's language!")
    "I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!"

    Challenge inputs:
    >>> encode('Tre Kronor är världens bästa ishockeylag.')
    'Totrore Kokrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeylolagog.'
    >>> encode('Vår kung är coolare än er kung.')
    'Vovåror kokunongog äror cocoololarore änon eror kokunongog.'
    """
    output = []
    for character in plaintext:
        if character.lower() in CONSONANTS:
            output.append(character + 'o' + character.lower())
        else:
            output.append(character)
    return ''.join(output)


def decode(in_text):
    """Decode text from Rövarspråket.

    Example inputs:

    >>> decode('Jojagog totalolaror Rorövovarorsospoproråkoketot!')
    'Jag talar Rövarspråket!'
    >>> decode("I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!")
    "I'm speaking Robber's language!"

    Challenge inputs:
    >>> decode('Totrore Kokrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeylolagog.')
    'Tre Kronor är världens bästa ishockeylag.'
    >>> decode('Vovåror kokunongog äror cocoololarore änon eror kokunongog.')
    'Vår kung är coolare än er kung.'
    """
    output = []
    index = 0
    while index < len(in_text):
        output.append(in_text[index])
        if in_text[index].lower() in CONSONANTS:
            index += 3
        else:
            index += 1
    return ''.join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
