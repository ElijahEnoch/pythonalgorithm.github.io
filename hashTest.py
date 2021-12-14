import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'hello world'.encode()
hash_object2 = hashlib.sha1()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)


def solution(phone_book):
    answer = True
    finish = False
    phone_book = sorted(phone_book, key=len)
    for i in range(0, len(phone_book)):
        if finish:
            break
        current = phone_book[i]
        for j in range(i+1, len(phone_book)):
            comp = phone_book[j]
            if len(current)<len(comp) and current == comp[0:len(current)]:
                answer = False
                finish = True
                break
    return answer

