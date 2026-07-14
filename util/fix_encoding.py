#!/usr/bin/env python3
"""
Script to fix file encoding by converting from UTF-16LE to UTF-8.
Takes a single file path as an argument and converts the encoding.
"""

import argparse
import sys
from pathlib import Path


def fix_encoding(file_path: str) -> None:
    """
    Convert a file to UTF-8 encoding. Handles both UTF-16LE (Windows)
    and UTF-8 (macOS/Linux) source files.
    
    Args:
        file_path: Path to the file to convert
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
        UnicodeDecodeError: If the file can't be decoded
        PermissionError: If there are permission issues with the file
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    content = None
    detected_encoding = None
    
    # Try UTF-8 first (macOS/Linux)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        detected_encoding = 'UTF-8'
        print(f"File is already UTF-8: {file_path}")
    except UnicodeDecodeError:
        # Try UTF-16LE (Windows)
        try:
            print(f"Converting {file_path} from UTF-16LE to UTF-8...")
            with open(path, 'r', encoding='utf-16le') as f:
                content = f.read()
            detected_encoding = 'UTF-16LE'
        except UnicodeDecodeError as e:
            print(f"Error: Could not decode file with UTF-8 or UTF-16LE: {e}")
            print("The file might be in an unsupported encoding or corrupted.")
            sys.exit(1)
    except PermissionError as e:
        print(f"Error: Permission denied accessing file: {e}")
        sys.exit(1)
    
    # Write back as UTF-8 if not already UTF-8
    try:
        if detected_encoding != 'UTF-8':
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully converted {file_path} from {detected_encoding} to UTF-8")
        else:
            print(f"No conversion needed: {file_path} is already UTF-8")
    except PermissionError as e:
        print(f"Error: Permission denied writing file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def main():
    """Main function to handle command line arguments and execute the conversion."""
    parser = argparse.ArgumentParser(
        description="Convert a file from UTF-16LE to UTF-8 encoding",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fix_encoding.py data.txt
  python fix_encoding.py /path/to/file.csv
        """
    )
    
    parser.add_argument(
        'file_path',
        help='Path to the file to convert from UTF-16LE to UTF-8'
    )
    
    args = parser.parse_args()
    
    try:
        fix_encoding(args.file_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()