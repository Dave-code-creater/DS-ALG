def char_to_index(ch: str) -> int:
    if ch == ' ':
        return 26
    return ord(ch) - ord('A')

def index_to_char(i: int) -> str:
    if i == 26:
        return ' '
    return chr(ord('A') + i)

def build_maps(plain: str, cipher: str):
    SIZE = 27
    encode_map = ['?'] * SIZE 
    decode_map = ['?'] * SIZE

    for i in range(len(plain)):
        p = plain[i]
        c = cipher[i]

        p_idx = char_to_index(p)
        c_idx = char_to_index(c)


        if encode_map[p_idx] == '?':
            encode_map[p_idx] = c
        elif encode_map[p_idx] != c:
            return None, None

        if decode_map[c_idx] == '?':
            decode_map[c_idx] = p
        elif decode_map[c_idx] != p:
            return None, None

    return encode_map, decode_map

def decode_line(line: str, decode_map) -> str:
    result = []
    for ch in line:
        c_idx = char_to_index(ch)
        mapped = decode_map[c_idx]
        if mapped == '?':
            result.append('.') 
        else:
            result.append(mapped)
    return ''.join(result)

sample_plain = "THERE ARE NOT ENOUGH LETTERS"
sample_cipher = "XQAZASEZASNYXSANYLWQSTAXXAZM"
target_cipher = "JSCENNYXSIACYIASXQJM"

encode_map, decode_map = build_maps(sample_plain, sample_cipher)
decoded = decode_line(target_cipher, decode_map)
print(decoded)

sample_plain = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
sample_cipher = "UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH"
target_cipher = "XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB"

encode_map, decode_map = build_maps(sample_plain, sample_cipher)
decoded = decode_line(target_cipher, decode_map)
print(decoded)