# cipher function
def cipher(text, shift, encrypt=True):
    '''
    Encrypts text by replacing each letter by a fixed position up or down the alphabet.

    Parameters
    ----------
    text: str
        A string.
    shift: int
        An integer.
    encrypt: bool
        A boolean.

    Returns
    -------
    new_text: str
        The encrypted text. 

    Examples
    --------
    >>> from cipher_cy2617 import cipher
    >>> text = str('Hello')
    >>> shift = int(1)
    >>> encrypt = True
    >>> cipher_cy2617.cipher('Hello', 1, True)
        'Ifmmp'
    >>> text = str('Ifmmp')
    >>> shift = int(1)
    >>> encrypt = False
    >>> cipher_cy2617.cipher('Hello', 1, False)
        'Hello'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text