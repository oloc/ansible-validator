# Ansible Validator

Ansible-validator test and validate **Ansible** roles with this:

* Syntax check
* A first apply
* A second apply to check idempotence

## Usage
A placer dans le répertoire du rôle à tester, puis procéder à un :

    ./validator

## Jenkins

If you want to use it with Jenkins, you have to add these lines below as a build script :

    rm -rf .git
    rm readme.md
    git init
    git remote add origin git@github.com:olo-dw/ansible-validator.git
    git fetch
    git checkout -t origin/master
    ./validator

## Prerequisites

* Docker
