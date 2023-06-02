import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('message', 'key')

    with pytest.raises(TypeError):
        encrypt_message(7, 20)

    assert encrypt_message("message", 7) == "egassem"

    assert encrypt_message("message", 3) == "sem_egas"

    assert encrypt_message("message", 4) == "ega_ssem"
