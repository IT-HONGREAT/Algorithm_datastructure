# Baekjoon
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857

import hashlib

string = input()
encoded =  string.encode()

sha = hashlib.sha256(encoded).hexdigest()

print(sha)