import hashlib
import sys
import os

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        fileContent = f.read()
        hash_md5.update(fileContent)
    return hash_md5.hexdigest()


print(sys.argv[0])
fileName = "/home/ec2-user/environment/Python/Tests/FileForMD5.txt"
print(md5(fileName))

print(os.path.dirname(os.path.abspath(sys.argv[0])))
