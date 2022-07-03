
def test_first_state(create_card1):
    response = create_card1.send('A4 20 00 00 00')
    assert response == '63 C5'


def test_invalid_cla(create_card1):
    response = create_card1.send('20 20 00 00 00')
    assert response == '63 00'


def test_invalid_ins(create_card1):
    response = create_card1.send('A4 56 00 00 00')
    assert response == '63 00'


def test_second_state(create_card1):
    response = create_card1.send('A4 20 00 00 00')
    assert response == '63 C3'


def test_invalid_p1(create_card1):
    response = create_card1.send('A4 20 01 00 00')
    assert response == '6A 86'


def test_invalid_p2(create_card1):
    response = create_card1.send('A4 20 00 03 00')
    assert response == '6A 86'


def test_third_state(create_card1):
    response = create_card1.send('A4 20 00 00 00')
    assert response == '63 C3'


def test_incorrect_pin(create_card1):
    response = create_card1.send('A4 20 00 01 04 00 00 00 00')
    assert response == '63 00'


def test_block_card(create_card1):
    for i in range(2):
        response = create_card1.send(str(i))
    assert response == '69 83'