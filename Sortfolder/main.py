import os
import asyncio
import shutil
import logging
import argparse
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def read_folder(src_folder, dest_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            await copy_file(os.path.join(root, file), dest_folder)

async def copy_file(file_path, dest_folder):
    file_extension = Path(file_path).suffix[1:]  # Get the file extension without the dot
    dest_path = Path(dest_folder) / file_extension
    
    dest_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(file_path, dest_path)
    logging.info(f'Copied {file_path} to {dest_path}')

def main():
    parser = argparse.ArgumentParser(description="Sort files based on their extensions.")
    parser.add_argument('src_folder', type=str, help="Source folder to read files from.")
    parser.add_argument('dest_folder', type=str, help="Destination folder to store sorted files.")
    args = parser.parse_args()

    asyncio.run(read_folder(args.src_folder, args.dest_folder))

if __name__ == "__main__":
    main()
