d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
d2 = {'C': 'W', '3': 'W', 'F': 'W', '0': 'T', '2': 'T', '4': 'T', 'B': '.', '+': '.', ';': '.', 'Q': '^', '7': '^', '8': '^', 'D': 'E', '1': 'E', 'Z': 'E', '(': 'M', ')': 'M', '9': 'M', '*': ':', '|': ':', '#': ':', 'X': ' ', 'P': ' ', '!': ' '}

def decipher_message(msg,guide):
    ans = ''
    for i in msg:
        if i in guide:
            ans += guide[i]
        else:
            ans += i
    return ans
 
def decode_map(mapfile,ddict,outfile):
    fp = open(mapfile)
    msg = fp.readlines()
    fp.close()
    out_msg = []
    for line in msg:
        out_line = decipher_message(line, ddict)
        out_msg.append(out_line)
    fp = open(outfile, 'w')
    fp.writelines(out_msg)
    fp.close()
        
def find_treasure(mapfile):
    fp = open(mapfile)
    msg = fp.readlines()
    fp.close()
    for i, line_i in enumerate(msg):
        if i == 0 or i == len(line_i) - 1:
            continue
        for pos in range(len(line_i) - 2):
            if line_i[pos: pos + 3] == 'TTT':
                if msg[i - 1][pos + 1] == 'T' and msg[i + 1][pos + 1] == 'T':
                    return (i, pos + 1)

print("Map 1")
decode_map('encoded_map.txt',d1,'decoded_map.txt')
print(find_treasure('decoded_map.txt'))

# Uncomment the following for your test cases

print("Map 2")
decode_map('encoded_map2.txt',d1,'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt',d1,'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt',d1,'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt',d2,'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))
