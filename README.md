﻿# passwordManager using CLI
 
## Overview
A Password Manager to securely manage and store passwords with username, password, email and app_name fields. A Master Password is used to authenticate into the manager "Vault", where all other passwords are stored.

## Requried Libraries
* Hashlib
* [Cryptodome](https://pypi.org/project/pycryptodome/)
* [pbkdf2](https://pypi.org/project/pbkdf2/)
* [psycopg2](https://pypi.org/project/psycopg2/)
* os
* [getpass](https://pypi.org/project/getpass3/)
* sys

# Setup
## step 1: Clone Project and Project Files
git clone https://github.com/dholendar14/passwordManager.git

## Step 2: Generate a Master Password Hash
Generate a master hash by using `master_password_hash_generator` and replace in the `password_hashing.py` file

## step 3: Salt value
Replace the salt value in `password_hashing.py` file

## Step 4: Connect to Docker Container
Enter in correct username, database name, and password inside the db_connect.py file.

## Step 5: Run Main.py
Run main.py with all files inside the same directory.
```
python3 main.py 
```
