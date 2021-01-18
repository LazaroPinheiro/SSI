import json

from models.user import user


def load_configs():
    with open("resources/config.json") as json_data_file:
        return json.load(json_data_file)


if __name__ == '__main__':
    #u = user('joao', 913136226)
    n = '3519342346'
    x = user.validatePhoneNumber(n)

    print(x)
    #u = user_management("resources/users.txt")
    #u.addNewUser('artur', '913136226')
    #print(u.getNumber('armindo'))
    # call("sh setup/setup.sh", shell=True)
    #jsonData = load_configs()

