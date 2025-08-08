import sys
import shutil
import os

if len(sys.argv) != 3:
    print("Usage: python3 backup.py <src> <dest>")
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

if not os.path.exists(src):
    print(f"Source path {src} does not exist")
    sys.exit(1)

shutil.copy(src , dest)
print(f"Backup completed from {src} to {dest}")
