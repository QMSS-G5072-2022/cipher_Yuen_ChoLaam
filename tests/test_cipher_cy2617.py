from cipher_cy2617 import cipher_cy2617

# test for symbols
def test_cipher_symbols():
    assert cipher_cy2617.cipher('smarties@hotmail.com', 2) == 'uoctvkgu@jqvockn.eqo'