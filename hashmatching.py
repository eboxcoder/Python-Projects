# Created by Avnish Singh - IN
import hashlib

filepath = "/Users/avnish/PycharmProjects/AIWC/pwd.txt"
filepath1 = "/Users/avnish/PycharmProjects/AIWC/hash.txt"
filepath2 = "/Users/avnish/PycharmProjects/AIWC/newpwd.txt"

pwdfile = open(filepath,"w")
pwdfile.writelines(["00000000\n",'admin\n','admin@123\n','11111111\n','12345678\n','987654321\n','0123456789\n','Password\n','passw0rd\n'])
pwdfile.close()

#with open(filepath,"r") as pwdfile:
#   print(pwdfile.read())

hash_list =[]

pwdfile = open(filepath, "r")
for i in pwdfile:
    passwd = i.strip()
    passwd_encode = passwd.encode()
    h1 = hashlib.sha512()
    h1.update(passwd_encode)
    pass_hash = h1.hexdigest()
    hash_list.append(pass_hash)
    print("Hash of\t:",i,"is\t:", pass_hash)

pwdfile.close()

#print(hash_list)

hash_file = open(filepath1, "w")
for i in hash_list:
    hash_file.writelines([i,"\n"])
hash_file.close()

#with open(filepath1,"r") as hash_file:
#   print(hash_file.read())

newpwd_file = open(filepath2,"w")
pwdlist=["00000000\n","admin\n","12345\n","passw0rd\n","ak1234\n"]
newpwd_file.writelines(pwdlist)
newpwd_file.close()

#with open(filepath2,"r") as newpwd_file:
#    print(newpwd_file.read())

hash_file = open(filepath1,"r")
newpwd_file = open(filepath2,"r")

for hash_loop in hash_file:
    hash_loop_strip = hash_loop.strip()
    #print("\n",hash_loop_strip)
    for pwd_loop in newpwd_file:
        passwd1 = pwd_loop.strip()
        passwd1_encode = passwd1.encode()
        h2 = hashlib.sha512()
        h2.update(passwd1_encode)
        hash_digest = h2.hexdigest()
       # print("\n",passwd1,"\t:",hash_digest,"\n")
        if (hash_loop_strip == hash_digest):
            print("\nPassword matches\t:",passwd1)
            break

print("\n\nNo other password matches")

hash_file.close()
newpwd_file.close()

