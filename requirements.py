#!/usr/bin/env python
#
# Argument: The role directory
#
# Olivier Locard

import os, sys
import yaml, tempfile

role = sys.argv[1]

file = open(role + "/meta/main.yml", "r")
content = yaml.load_all(file)

with tempfile.NamedTemporaryFile(delete = False, suffix='.yml') as fileTemp:
    fileTemp.write("---\n")
    for entry in content:
        for dependency in entry["dependencies"]:
            dep_str= str(dependency)
            print "Dependency: ", dep_str
            fileTemp.write("- "+dep_str+"\n")

    os.system("ansible-galaxy install -r "+fileTemp.name)

fileTemp.close()


