"""
File: user_create.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-22
Description: Script to create a new user with specified roles and groups.
"""

import subprocess
import sys

def main():
    full_name = input("Enter your full name: ")
    
    print("1. User")
    print("2. AV Tech") 
    print("3. Admin")
    role = input("Select your role: ")
    
    username = full_name.lower().replace(' ', '-')
    
    groups_add = ""
    
    if role == "1":
        group = "user"
    elif role == "2":
        group = "avtech"
        groups_add = "audio,video"
    elif role == "3":
        group = "admin"
        groups_add = "root"
    else:
        print("Invalid role selected.")
        sys.exit(1)
    
    print(f"Created user {username} with role {role}")
    
    cmd = ["sudo", "useradd", "-m", "-c", full_name]
    
    if groups_add:
        cmd.extend(["-G", groups_add])
    
    cmd.append(username)
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully created user: {username}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: sudo command not found. Make sure you have sudo privileges.")
        sys.exit(1)

if __name__ == "__main__":
    main()
