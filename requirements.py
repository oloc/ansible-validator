#!/usr/bin/env python
#
# Argument: The role directory
#
# Olivier Locard

import os, sys
import yaml

role = sys.argv[1]

file = open(role+"/meta/main.yml", "r")
content = yaml.load_all(file)

for entry in content:
  for dependency in entry["dependencies"]:
    print "Dependency: ", dependency
    os.system("ansible-galaxy install "+dependency)
