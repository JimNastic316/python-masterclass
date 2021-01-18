data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]
#
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))

def simple_hash(s: str) -> int:
    """
    Simple hash function
    :param s: string
    :return:
    """
    basic_hash = ord(s[0])
    return basic_hash % 10

def get(k: str) -> str:
    """
    Return the value for a key, or None if the key doesn't exist
    :param k: Key value to be checked
    :return: value for key or None
    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)  <-- python version of hash
    print(key, h)
    keys[h] = key
    values[h] = value

print(f"Keys: {keys}")
print(f"Values: {values}")
print()
value = get("banana")
print(f"Value :{value}")