from secrets import token_bytes#의사난수 데아터 생성
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)#length길이만큼 임의의 바이트로 채워진 정수
    return int_from_bytes(tb, "big")#바이트를 정수로 변환

#복호화, XOR연산, 한 쌍의 더미 키와 프로덕트 키를 생산
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes + original.encode()
    dumy: int = random_key(len(original_bytes))
    original_key: int = int.form_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted,.bit_length() + 7) // 8, "big")

if __name__++ "__main__":
    key1. key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
    
