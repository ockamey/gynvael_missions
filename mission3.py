import itertools
import string
import math

huffman_coding_mappings = [
{
    "1": "A",
    "01": "B",
    "000": "C",
    "001": "D",
},
{
    "1": "A",
    "00": "B",
    "010": "C",
    "011": "D",
},
{
    "0": "A",
    "10": "B",
    "110": "C",
    "111": "D",
},
{
    "0": "A",
    "11": "B",
    "101": "C",
    "100": "D",
}]

cipher = "10101011101000110100011101111111011111110111010010110010011100101111001011001001101110011010001110111111101001011110100111011110110010110010011101010111101100111110101111101111011110111101110111111100101100100101100100111011001110010110010011010001110110011110110100101100100110111001110010111"
results_with_assumptions : list[str] = []

def get_possible_pseduo_quadra_numbers() -> list[str]:
    results = []
    for huffman_coding_mapping in huffman_coding_mappings:
        bit_word = ""
        result = ""
        for bit in cipher:
            bit_word += bit
            if bit_word in huffman_coding_mapping:
                result += huffman_coding_mapping[bit_word]
                bit_word = ""
        if bit_word != "":
            raise Exception()
        for perm in itertools.permutations(["0", "1", "2", "3"]):
            results.append(result.replace("A", perm[0]).replace("B", perm[1]).replace("C", perm[2]).replace("D", perm[3]))
    return results

def get_bytes_of_quadra_nums(quadra_nums):
    results = []
    for quadra_num_str in quadra_nums:
        bytes_len = math.ceil(len(quadra_num_str) * 2 / 8)
        num = int(quadra_num_str, 4)
        num_bytes = num.to_bytes(bytes_len, 'little')
        results.append(num_bytes)
    return results

def print_printable_words(bytes_results):
    for result in bytes_results:
        try:
            decoded_str = result.decode()
        except:
            continue
        if all([char in string.printable for char in decoded_str ]):
            print(decoded_str)

quadra_nums = get_possible_pseduo_quadra_numbers()
bytes_results = get_bytes_of_quadra_nums(quadra_nums)
print_printable_words(bytes_results)
