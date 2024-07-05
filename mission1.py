import hashlib

xored_hash_str = "76fb930fd0dbc6cba6cf5bd85005a92a"
xored_hash_bytes = bytes.fromhex(xored_hash_str)


with open("/home/ockamey/code/gyn/mission1/words_alpha.txt", "r") as file:
    words_str = file.read()

words = words_str.split('\n')

hashed_words_dict = { hashlib.md5(w.encode()).digest(): w for w in words if len(w) == 8 }

for hashed_word_bytes in hashed_words_dict:
    second_hash_bytes = bytes([a ^ b for a, b in zip(xored_hash_bytes, hashed_word_bytes)])

    if second_hash_bytes in hashed_words_dict:
        print(f"Found: {hashed_words_dict[hashed_word_bytes]}, {hashed_words_dict[second_hash_bytes]}")
        break
