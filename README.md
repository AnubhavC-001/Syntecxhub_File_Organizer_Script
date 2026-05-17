# File Organizer Script

A complete professional Python automation project to automatically organize your files by their extension into structured categories.

## Project Overview

Are your downloads or document folders a mess? This script automatically scans a specified folder and organizes all files into categorized subfolders based on their file extensions (e.g., Images, Documents, Videos, etc.).

## Features

- **Automated Sorting:** Automatically categorizes files by extension into specific folders.
- **Duplicate Handling:** Safely handles duplicate filenames by appending a numerical counter (e.g., `file_1.txt`).
- **Dry-run Mode:** Preview what files will be moved and where, without actually moving them.
- **Logging Support:** Keeps a record of all moved files in a dedicated log file (`logs/moved_files.log`).
- **Colored Output:** Uses `colorama` to display clear, color-coded terminal messages for better readability.
- **Customizable:** Easily add new categories and file extensions to the configuration.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnubhavC-001/Syntecxhub_File_Organizer_Script.git
   cd Syntecxhub_File_Organizer_Script
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. Place the files you want to organize inside the `test_folder` directory.
2. Run the script:
   ```bash
   python organizer.py
   ```
3. To run in dry-run mode (simulate without moving files):
   ```bash
   python organizer.py --dry-run
   ```
4. Check the `organized_files` directory to see your sorted files.

## Automating & Scheduling (Desktop Cleanup)

To make this a fully automated background cleanup tool, you can schedule it to run automatically.

### 🪟 Windows (Task Scheduler)
To run the script automatically every day or at startup:
1. Press `Win + R`, type `taskschd.msc`, and press **Enter** to open the Windows Task Scheduler.
2. Click **Create Basic Task...** in the right-hand panel.
3. Name the task (e.g., `Desktop File Organizer`) and set the trigger to **Daily** or **At Log On**.
4. Set Action to **Start a Program**.
5. Configure the program:
   - **Program/script:** `F:\SYNTEC\file-organizer-script\venv\Scripts\python.exe`
   - **Add arguments:** `organizer.py`
   - **Start in:** `F:\SYNTEC\file-organizer-script\`
6. Click **Finish**. Now, your workspace is organized automatically!

### 🐧 Linux & macOS (Cron Job)
To schedule it on Unix systems, open your terminal and edit your crontab:
```bash
crontab -e
```
Add the following line to automatically run the script every day at 12:00 PM:
```bash
0 12 * * * /absolute/path/to/venv/bin/python /absolute/path/to/file-organizer-script/organizer.py
```

## Future Improvements

- Add a graphical user interface (GUI) using Tkinter or PyQt.
- Support for recursive scanning (organizing files in subfolders).
- Configuration file (JSON/YAML) for easier customization by non-programmers.
- Add an undo feature to revert the last organization run.

