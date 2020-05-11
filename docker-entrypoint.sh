#!/bin/bash

echo ""
echo ""

CONFIG="/app/config/settings.py"

if [ -e "$CONFIG" ]; then
    echo "Using $CONFIG"
    echo ""
    echo ""
else
    mkdir -p /app/config
    touch /app/config/__init__.py

    echo "Creating $CONFIG"
    echo ""
    echo ""

/bin/cat <<-EOF > "$CONFIG"
# Rename settings_sample.py to settings.py
# Generate jss_credentials with:
# printf "username:password" | iconv -t ISO-8859-1 | base64 -i -

jss_server = "YOUR_JAMF_PRO_URL"
jss_credential = "YOUR_CREDENTIALS"

attributes = {
    "extension_attributes": [
        {
            "id": 32,                       # Extenssion attribute ID
            "name": "shared_computer",      # Name in API output
        },
        {
            "id": 11,
            "name": "Whetever..."
        }
    ]
}
EOF

fi

# Hand off to the CMD
exec "$@"