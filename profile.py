path = 'profiles/'
remaning_likes = 50
profile = dict()

def setNewProfile():
    profile['name'] = str(input('Enter profile name: '))
    profile['token'] = str(input('Add Tinder token: '))
    profile['like'] = remaning_likes
    return profile

def saveProfile(name, token, like):
    profile = open(path + name + ".profile", "w")
    profile.write(name + "\n" + token + "\n" + str(like) )
    profile.close()

def loadProfile(name):
    f = open(path + name + ".profile", "r")
    temp = f.read().splitlines()
    profile['name'] = temp[0]
    profile['token'] = temp[1]
    profile['like'] = int(temp[2])
    return profile