

## link >> https://cybertalents.com/challenges/cryptography/postbase

import base64 
encoded_text = "BR3tCNDUzXzYxWDdZXzRSfQ=="

char_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_lower = char_upper.lower()
numbers = "0123456789"
signs = "+/"
all = char_lower + char_upper + numbers +signs

for i in range(64):
    for j in range(64):
        final_encoded= 'R' + all[i] + all[j] + encoded_text 
        decode_text=base64.b64decode(final_encoded)
        if b'FLAG' in decode_text:
            print(decode_text)
            

