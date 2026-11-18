
#!/bin/bash

echo "=================================="
echo "       SSH SECURITY AUDIT"
echo "=================================="

# Check whether SSH is installed
if ! command -v sshd >/dev/null 2>&1; then
    echo "[ERROR] SSH server is not installed."
    exit 1
fi

# Read effective SSH configuration
CONFIG=$(sudo sshd -T)

check_setting() {
    KEY="$1"
    EXPECTED="$2"

    VALUE=$(echo "$CONFIG" | grep -i "^${KEY} ")

    echo "$VALUE"

    if [ "$VALUE" = "${KEY} ${EXPECTED}" ]; then
        echo "[PASS] $KEY is configured correctly."
    else
        echo "[REVIEW] $KEY requires attention."
    fi

    echo
}

echo "--- Authentication Settings ---"

check_setting "permitrootlogin" "no"
check_setting "pubkeyauthentication" "yes"
check_setting "maxauthtries" "3"

echo "=================================="
echo "         AUDIT COMPLETED"
echo "=================================="

