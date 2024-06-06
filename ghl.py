plaintext = 'COMPUTERSECURITY'
key = 'ghcipher'


ip_table = [58,  50,  42,  34,  26,  18,  10,  2,
            60,  52,  44,  36,  28,  20,  12,  4,
            62,  54,  46,  38,  30,  22,  14,  6,
            64,  56,  48,  40,  32,  24,  16,  8,
            57,  49,  41,  33,  25,  17,  9,   1,
            59,  51,  43,  35,  27,  19,  11,  3,
            61,  53,  45,  37,  29,  21,  13,  5,
            63,  55,  47,  39,  31,  23,  15,  7,
            122, 114, 106, 98,  90,  82,  74,  66,
            124,  116,  108,  100,  92,  84,  76,  68,
            126, 118, 110, 102, 94, 86, 78, 70,
            128, 120, 112, 104, 96,  88,  80,  72,
            121, 113, 105, 97,  89,  81,  73,  65,
            123, 115, 107, 99,  91,  83,  75,  67,
            125,  117,  109,  101,  93, 85, 77, 69,
            127, 119, 111, 103, 95, 87, 79, 71]


key_perm_table = [49, 23, 9, 14, 3, 59, 40, 45,
                  33, 1, 25, 16, 7, 60, 52, 64,
                  4, 48, 6, 22, 38, 24, 8, 57,
                  19, 63, 43, 31, 2, 41, 27, 18,
                  55, 36, 32, 29, 46, 47, 5, 15,
                  12, 62, 50, 30, 44, 61, 28, 34,
                  39, 26, 54, 20, 21, 17, 42, 56,
                  35, 37, 11, 10, 58, 51, 13, 53]


key_comb_table = [25, 48, 17, 12, 27, 6, 53, 41,
                  50, 61, 28, 31, 10, 19, 7, 45,
                  57, 4, 20, 21, 59, 34, 11, 46,
                  18, 35, 43, 2, 56, 47, 23, 32,
                  58, 40, 51, 63, 29, 3, 5, 22,
                  64, 26, 44, 49, 55, 37, 13, 16,
                  42, 38, 30, 8, 9, 54, 52, 33,
                  14, 60, 1, 24, 15, 39, 36, 62]

matrix_perm = [12, 3, 7, 14,
               8, 1, 16, 5,
               9, 4, 11, 15,
               6, 10, 2, 13]

shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]


s_boxes = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],


           [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],


           [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],


           [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]]


f_final_perm = [23, 45, 12, 8, 33, 10, 7, 55,
                31, 21, 29, 4, 46, 50, 38, 13,
                1, 6, 53, 47, 26, 18, 36, 14, 30,
                24, 32, 28, 39, 17, 64, 57, 58,
                2, 44, 34, 48, 25, 49, 15, 20,
                9, 59, 5, 22, 3, 27, 54, 37,
                41, 56, 19, 40, 60, 52, 16, 35,
                62, 61, 11, 42, 63, 51, 43]


fp_table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55,
            23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5,
            45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60,
            28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10,
            50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25, 104,
            72, 112, 80, 120, 88, 128, 96, 103, 71, 111, 79, 119,
            87, 127, 95, 102, 70, 110, 78, 118, 86, 126, 94, 101,
            69, 109, 77, 117, 85, 125, 93, 100, 68, 108, 76, 116,
            84, 124, 92, 99, 67, 107, 75, 115, 83, 123, 91, 98, 66,
            106, 74, 114, 82, 122, 90, 97, 65, 105, 73, 113, 81, 121, 89]


def convert_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def permute(text, table):
    res = ''
    for num in table:
        res += text[num - 1]
    return res


def left_shift(bin_str, n_shift):
    shifted = ''
    for _ in range(n_shift):
        for j in range(1, len(bin_str)):
            shifted += bin_str[j]
        shifted += bin_str[0]
        bin_str = shifted
        shifted = ""
    return bin_str


def get_keys(key):
    keys = []
    key = permute(key, key_perm_table)
    left = key[:32]
    right = key[32:]
    for i in range(16):
        tmp = right
        right = xor_string(right, left)
        left = tmp
        left = left_shift(left, shift_table[i])

        keys.append(permute(left + right, key_comb_table))

    return keys


def xor_string(str1, str2):
    res = ''
    for i in range(len(str1)):
        res += '0' if str1[i] == str2[i] else '1'

    return res


def s_box_operations(m):
    for i in range(4):
        for j in range(4):
            row = int(m[i][j][0] + m[i][j][3], 2) ^ j
            col = int(m[i][j], 2)
            m[i][j] = format(s_boxes[i][row][col], '04b')


def make_matrix(R):
    matrix = [['0'] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = R[i * 16 + j * 4: i * 16 + j * 4 + 4]

    return matrix


def matrix_shuffle(m):
    shuffled = [['0'] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            elem = matrix_perm[i * 4 + j]
            row = (elem - 1) // 4
            col = (elem - 1) % 4
            shuffled[i][j] = m[row][col]
    return shuffled


def shift_matrix_left(m):
    for i in range(3):
        for _ in range(i + 1):
            tmp = m[i][0]
            for j in range(3):
                m[i][j] = m[i][j + 1]
            m[i][3] = tmp


def back_to_str(m):
    R = ''
    for i in range(4):
        for j in range(4):
            R += m[i][j]

    return R


def f(R, K):
    m = make_matrix(R)
    m = matrix_shuffle(m)
    s_box_operations(m)
    shift_matrix_left(m)
    R = back_to_str(m)
    return permute(R, f_final_perm)


def shift_left(k, nth_shifts):
    s = ""
    for _ in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k


def ghl_encryption(plaintext, key, enc):
    permute_plaintext = permute(plaintext, ip_table)
    keys = get_keys(key)

    if not enc:
        keys = keys[::-1]

    L = permute_plaintext[:64]
    R = permute_plaintext[64:]
    for i in range(16):
        L, R = R, xor_string(L, f(R, keys[i]))
        print(f"Round {i + 1}:\nLeft: {L} Right: {R}")
    cipher = permute(R + L, fp_table)
    return cipher


print("Encryption")
plaintext = convert_to_binary(plaintext)
key = convert_to_binary(key)
ciphertext = ghl_encryption(plaintext, key, enc=True)
print(f'Ciphertext: {ciphertext}')
print(f'Ciphertext: {hex(int(ciphertext, 2))}')


print("Decryption")
plaintext_decrypted = ghl_encryption(ciphertext, key, dec=False)
print(f'Plaintext: {plaintext_decrypted}')
print(f'Plaintext: {hex(int(plaintext_decrypted, 2))}')

print(plaintext == plaintext_decrypted)
print(hex(int(plaintext, 2)), hex(int(plaintext_decrypted, 2)))
