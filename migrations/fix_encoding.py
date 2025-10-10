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
    Convert a file from UTF-16LE to UTF-8 encoding.
    
    Args:
        file_path: Path to the file to convert
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
        UnicodeDecodeError: If the file can't be decoded as UTF-16LE
        PermissionError: If there are permission issues with the file
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    print(f"Converting {file_path} from UTF-16LE to UTF-8...")
    
    try:
        # Read the file with UTF-16LE encoding
        with open(path, 'r', encoding='utf-16le') as f:
            content = f.read()
        
        # Write the file back with UTF-8 encoding
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully converted {file_path} to UTF-8")
        
    except UnicodeDecodeError as e:
        print(f"Error: Could not decode file as UTF-16LE: {e}")
        print("The file might not be in UTF-16LE encoding or might be corrupted.")
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: Permission denied accessing file: {e}")
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