# Name:         user_create.sh
# Author:       Reagan Zierke <reagan.zierke@example.com>
# Created:      2025-09-14
# Description:  Script to create a new user with specified roles and groups. 

#!/bin/bash

echo "Enter your full name: "
read FULL_NAME
echo "1. User\n2. AV Tech\n3. Admin\n Select your role: "
read ROLE

USERNAME=$(echo "$FULL_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

GROUPS_ADD=""
case $ROLE in
    1)
        GROUP="user"
        ;;
    2)
        GROUP="avtech"
        GROUPS_ADD="audio,video"
        ;;
    3)
        GROUP="admin"
        GROUPS_ADD="root"
        ;;
    *)
        echo "Invalid role selected."
        exit 1
        ;;
esac

echo "Created user $USERNAME with role $ROLE"
sudo useradd -m -c "$FULL_NAME" -G "$GROUPS_ADD" "$USERNAME"
