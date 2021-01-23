import json
import sys
from subprocess import call

from fuse import FUSE

from business import user_manager
from business.passthrough import Passthrough
from models.configurations import configurations


def load_configurations():
    with open("resources/config.json") as json_data_file:
        jsonString = json.load(json_data_file)
        return configurations(jsonString['sms_sender']['sourceName'], jsonString['sms_sender']['nexmo']['key'],
                              jsonString['sms_sender']['nexmo']['secret'], jsonString['token_generator']['token_size'],
                              jsonString['user_manager']['pathUsersFile'])


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Insufficient Number Of Arguments!")

    # call("sh setup/setup.sh", shell=True)
    configurations = load_configurations()
    root = sys.argv[1]
    mountpoint = sys.argv[2]
    FUSE(Passthrough(root, configurations), mountpoint, nothreads=True, foreground=True)
