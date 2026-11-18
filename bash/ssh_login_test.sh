
#!/bin/bash

echo "=================================="
echo "         SSH LOGIN TEST"
echo "=================================="

read -p "Ubuntu Server IP: " SERVER
read -p "Username: " USERNAME

echo
echo "Connecting to $SERVER..."
echo "Use your normal SSH credentials."
echo

ssh -o ConnectTimeout=5 \
    -o NumberOfPasswordPrompts=1 \
    "$USERNAME@$SERVER"

echo
echo "SSH session ended."

