#!/data/data/com.termux/files/usr/bin/bash

echo "📦 Installing CodeBlocks CLI..."

# Copy file client ke bin sistem
cp client/cblock.sh $PREFIX/bin/cblock

# Kasih izin eksekusi
chmod +x $PREFIX/bin/cblock

echo "✅ Completed : You can now use command 'cblock'."
echo "Cobain: cblock tests/test.lua"
