class Card:
    def __init__(self):
        self.isblocked = False
        self.isauth = False
        self.retry_counter = 5
        self.glob_pin = '01 09 04 07'

    def send(self, hex_data_string):
        if not self.isblocked:
            self.com = hex_data_string.split(maxsplit=5)
            return self.check_commands(self.com[0], self.com[1])

    def check_commands(self, cla, ins):
        if cla == 'A4' and ins == '20':
            return self.check_params(self.com[2], self.com[3])
        return self.check_counter()

    def check_params(self, p1, p2):
        if p1 == '00' and p2 == '00':
            if self.isauth:
                return '90 00'
            else:
                a = '63 C' + str(self.retry_counter)
                return a
        elif p1 == '00' and p2 == '01':
            return self.check_lc_data(self.com[4], self.com[5:])
        else:
            return '6A 86'

    def check_lc_data(self, lc, data):
        if lc == '04' and data[0] == self.glob_pin:
            self.retry_counter = 5
            self.isauth = True
            return '90 00'
        return self.check_counter()

    def check_counter(self):
        self.retry_counter -= 1
        if self.retry_counter:
            return '63 00'
        return '69 83'


if __name__ == '__main__':
    c = Card()
    q = 'A4 20 00 01 04 01 09 04 07'
    print(c.send(q))
