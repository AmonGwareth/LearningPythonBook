
import hashlib

md5_key = hashlib.md5('abcdef609043'.encode())

print(md5_key.hexdigest())

from MD5_miner import MD5Miner

md5_miner = MD5Miner()

md5_miner.start_mining()

# print(md5_miner.current_num)

# long mining

md5_miner_long = MD5Miner('000000')

md5_miner_long.start_mining()