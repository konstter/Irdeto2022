
def test_valid_pin(create_card2):
    response = create_card2.send('A4 20 00 01 04 01 09 04 07')
    assert response == '90 00'


def test_check_state(create_card2):
    response = create_card2.send('A4 20 00 00 00')
    assert response == '90 00'
