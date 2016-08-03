# Ansible Validator

Ansible-validator test and validate **Ansible** roles with this:

* Syntax check
* A first apply
* A second apply to check idempotence

## Usage
Copy all the stuff into the Ansible role directory and run :

    ./validator

### tests
By default the test is the one in the _defaults_ directory. But you can setup a _tests_ directory into your projet repository with your own tests. Dynamically the _validator_ will use them.

You just have to set some special vars in order to create your use case into the pattern below:

    ---
    - hosts: all
      vars: <= Here you can set some special vars in order to perform some use case
      roles:
        - role_under_test

### Systems
The tests are applied on the **docker** systems (which are defined in the _dockerfiles_ directory).
You can select a part of this systems by creating the file named _validator.list_ containing the list of your selection.

Example of _validator.list_:

    debian-8
    ubuntu-16.04

## Jenkins

If you want to use it with Jenkins, you have to add these lines below as a build script :

    rm -rf .git
    rm readme.md
    git init
    git remote add origin git@github.com:olo-dw/ansible-validator.git
    git fetch
    git checkout -t origin/master
    ./validator

## Prerequisites

* Docker
