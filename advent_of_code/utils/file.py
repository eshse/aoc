from pathlib import Path

def get_contents(filepath):
    """Read file contents and return as list of stripped lines."""
    file_path = Path(filepath)
    if not file_path.is_absolute():
        # If relative path, assume it's relative to project root
        file_path = Path(__file__).parent.parent.parent / filepath
    
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_raw_contents(filepath):
    """Read file contents and return as raw string."""
    file_path = Path(filepath)
    if not file_path.is_absolute():
        # If relative path, assume it's relative to project root
        file_path = Path(__file__).parent.parent.parent / filepath
    
    with open(file_path) as f:
        return f.read()