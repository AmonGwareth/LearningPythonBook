import hashlib


class MD5Miner:

    def __init__(self, leading_string: str = '00000'):
        self.md5_hash = ''
        self.secret_key = 'ckczppom'
        self.current_num = 0
        self.correct_key_mined = False
        self.leading_string = leading_string

    def mine_new_hash(self):
        input_key = self.secret_key + str(self.current_num)
        self.md5_hash = hashlib.md5(input_key.encode()).hexdigest()
        self.current_num += 1

    def start_mining(self):
        while not self.correct_key_mined:
            self.mine_new_hash()
            if self.md5_hash.startswith(self.leading_string):
                self.correct_key_mined = True
                print(f'We Found the key: {self.md5_hash} with a input of {self.current_num - 1}')
