"""
Main script to organize files by extension.
"""
import os
import shutil
from colorama import init, Fore, Style
from config import SOURCE_DIR, DESTINATION_DIR, EXTENSION_MAPPING
from logger import logger

# Initialize colorama for colored terminal output
init(autoreset=True)

def get_category(extension):
    """Returns the category for a given file extension."""
    for category, extensions in EXTENSION_MAPPING.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def handle_duplicate(destination_path):
    """Handles duplicate filenames by appending a number to the filename."""
    if not os.path.exists(destination_path):
        return destination_path
        
    base_name, ext = os.path.splitext(destination_path)
    counter = 1
    
    # Keep incrementing counter until a unique filename is found
    while os.path.exists(f"{base_name}_{counter}{ext}"):
        counter += 1
        
    return f"{base_name}_{counter}{ext}"

def organize_files(dry_run=False):
    """Scans the source directory and organizes files into categorized folders."""
    
    if not os.path.exists(SOURCE_DIR):
        print(Fore.RED + f"Error: Source directory '{SOURCE_DIR}' does not exist.")
        print(Fore.YELLOW + "Please create 'test_folder' and add some files to test.")
        return

    if dry_run:
        print(Fore.CYAN + "=== DRY RUN MODE: No files will be moved ===")

    # Get list of files in the source directory
    try:
        files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    except Exception as e:
        print(Fore.RED + f"Error reading source directory: {e}")
        logger.error(f"Error reading source directory: {e}")
        return

    if not files:
        print(Fore.YELLOW + f"No files found in '{SOURCE_DIR}' to organize.")
        return

    print(Fore.GREEN + f"Found {len(files)} files to organize.\n")

    moved_count = 0
    
    for filename in files:
        source_path = os.path.join(SOURCE_DIR, filename)
        
        # Extract the file extension
        _, ext = os.path.splitext(filename)
        
        # Determine the category based on the extension
        category = get_category(ext)
        
        # Create category directory path
        category_dir = os.path.join(DESTINATION_DIR, category)
        
        # Target destination path for the file
        target_path = os.path.join(category_dir, filename)
        
        # Handle duplicates if file already exists in destination
        target_path = handle_duplicate(target_path)
        
        final_filename = os.path.basename(target_path)
        
        if dry_run:
            print(Fore.BLUE + f"[DRY RUN] Would move: {filename} -> {category}/{final_filename}")
        else:
            try:
                # Ensure category directory exists
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                    
                # Move the file
                shutil.move(source_path, target_path)
                moved_count += 1
                
                print(Fore.GREEN + f"Moved: {filename} -> {category}/{final_filename}")
                logger.info(f"Moved '{source_path}' to '{target_path}'")
                
            except Exception as e:
                print(Fore.RED + f"Error moving {filename}: {e}")
                logger.error(f"Failed to move '{source_path}' to '{target_path}': {e}")

    if dry_run:
        print(Fore.CYAN + f"\n[DRY RUN] Total files that would be moved: {len(files)}")
    else:
        print(Fore.CYAN + f"\nSuccessfully moved {moved_count} files.")

if __name__ == "__main__":
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization process without moving files.")
    
    args = parser.parse_args()
    
    print(Style.BRIGHT + Fore.MAGENTA + "=== File Organizer Script ===\n")
    organize_files(dry_run=args.dry_run)
