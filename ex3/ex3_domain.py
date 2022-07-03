class Card:
    def __init__(self):
        self.isblocked = False
        self.isauth = False
        self.retry_counter = 5
        self.glob_pin = '01 09 04 07'

    def send(self, hex_data_string):
        if not self.isblocked:
            com = hex_data_string.split()
            if com[0] == 'A4' and com[1] == '20':
                if com[2] == '00' and com[3] == '00' and com[4] == '00':
                    if not self.isauth:
                        a = '63 C' + str(self.retry_counter)
                        return a
                    else:
                        return '69 00'
            self.retry_counter -= 1
            if self.retry_counter:
                return '63 00'
                
        return '69 83'