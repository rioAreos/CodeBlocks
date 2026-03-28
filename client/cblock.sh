#!/data/data/com.termux/files/usr/bin/bash

# Pastikan user input nama file
if [ -z "$1" ]; then
    echo "❌ Usage: cblock <file_name>"
    echo "Examples: cblock main.lua"
    exit 1
fi

# Cek apakah file ada di lokasi
if [ ! -f "$1" ]; then
    echo "❌ | '$1' Isnt Found"
    exit 1
fi

# Alamat server (Ganti IP ini dengan IP server/PC tempat kamu jalanin Flask)
# Jika jalanin di HP yang sama (lewat session Termux lain), gunakan localhost:5000
SERVER_URL="http://localhost:5000/execute"

echo "🚀 Sending $1 To CodBlock Server..."

# Kirim file via CURL
response=$(curl -s -X POST -F "file=@$1" $SERVER_URL)

echo "------------------------"
echo "OUTPUT SERVER:"
echo "$response"
echo "------------------------"
