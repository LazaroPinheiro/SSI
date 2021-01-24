import json
import os
import sys
from subprocess import call

from fuse import FUSE

from business.fuseController import FuseController
from models.configurations import configurations


def load_configurations():
    os.chmod("resources/config.json", 400)
    with open("resources/config.json") as json_data_file:
        jsonString = json.load(json_data_file)
        os.chmod("resources/config.json", 000)
        return configurations(jsonString['sms_sender']['sourceName'], jsonString['sms_sender']['nexmo']['key'],
                              jsonString['sms_sender']['nexmo']['secret'], jsonString['token_generator']['token_size'],
                              jsonString['user_manager']['pathUsersFile'], jsonString['fuse_controller']['timeout_time']
                              )


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Insufficient Number Of Arguments!")

    call("sh setup/setup.sh", shell=True)
    configurations = load_configurations()
    root = sys.argv[1]
    mountpoint = sys.argv[2]
    FUSE(FuseController(root, configurations), mountpoint, nothreads=True, foreground=True)
