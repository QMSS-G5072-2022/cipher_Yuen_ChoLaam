from cipher_cy2617 import cipher_cy2617
import numpy as np

# integration test
def test_cipher_integration():
    test_str = 'American Pie'
    shift_values = np.arange(1, 11)

    for i in shift_values:
        test_encrypt = cipher_cy2617.cipher(test_str, i, encrypt=True)
        test_decrypt = cipher_cy2617.cipher(test_encrypt, i, encrypt=False)
        assert test_str == test_decrypt