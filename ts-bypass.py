#!/usr/bin/env python3
"""
TeamSpeak 3 Blacklist Bypass & Cache Cleaner
Supports Windows, Linux, and macOS.
Requires administrator/root privileges to modify the hosts file.
"""

import os
import sys
import platform
import shutil
import time
import logging
from pathlib import Path
import ctypes

# ------------------------------
# Color constants (ANSI escape)
# ------------------------------
RESET = "\033[0m"
COLOR_MAP = {
    'DEBUG': '\033[36m',      # Cyan
    'INFO': '\033[32m',       # Green
    'WARNING': '\033[33m',    # Yellow
    'ERROR': '\033[31m',      # Red
    'CRITICAL': '\033[35m',   # Magenta
    'BANNER': '\033[1;36m',   # Bold Cyan
    'PROMPT': '\033[1;33m',   # Bold Yellow
}

# ------------------------------
# Custom colored log formatter
# ------------------------------
class ColoredFormatter(logging.Formatter):
    """Logging formatter that adds ANSI colors based on log level."""
    def format(self, record):
        log_color = COLOR_MAP.get(record.levelname, RESET)
        record.levelname = f"{log_color}{record.levelname}{RESET}"
        record.msg = f"{log_color}{record.msg}{RESET}"
        return super().format(record)

def setup_logger():
    """Create and configure the root logger with colored console output."""
    logger = logging.getLogger("TS3Bypass")
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    
    # Formatter
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    datefmt = "%H:%M:%S"
    formatter = ColoredFormatter(fmt, datefmt=datefmt)
    ch.setFormatter(formatter)
    
    # Avoid duplicate handlers if called multiple times
    if not logger.handlers:
        logger.addHandler(ch)
    return logger

log = setup_logger()

# ------------------------------
# Privilege check functions
# ------------------------------
def is_admin():
    """Return True if the script is running with administrator/root privileges."""
    system = platform.system().lower()
    if system == "windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    else:
        return os.geteuid() == 0

# ------------------------------
# Path utility functions
# ------------------------------
def get_hosts_path():
    """Return the path to the hosts file based on the operating system."""
    system = platform.system().lower()
    if system == "windows":
        return Path("C:\\Windows\\System32\\drivers\\etc\\hosts")
    else:
        return Path("/etc/hosts")

def get_cache_dir():
    """Return the path to the TeamSpeak 3 cache directory."""
    system = platform.system().lower()
    home = Path.home()

    if system == "windows":
        appdata = os.getenv("APPDATA", "")
        if appdata:
            return Path(appdata) / "TS3Client" / "cache"
        else:
            return home / "AppData" / "Roaming" / "TS3Client" / "cache"
    elif system == "darwin":  # macOS
        return home / "Library" / "Application Support" / "TeamSpeak 3" / "cache"
    else:  # Linux and others
        return home / ".ts3client" / "cache"

# ------------------------------
# Hosts file operations
# ------------------------------
def backup_hosts(hosts_path):
    """Create a backup of the hosts file with .bak extension."""
    backup_path = hosts_path.with_suffix(hosts_path.suffix + ".bak")
    try:
        shutil.copy2(hosts_path, backup_path)
        log.info(f"Backup created at: {backup_path}")
    except Exception as e:
        log.warning(f"Could not create backup: {e}")

def append_lines_to_hosts(hosts_path, lines):
    """
    Append the given lines to the hosts file if they do not already exist.
    Returns True if changes were made, False if already present.
    """
    try:
        content = hosts_path.read_text(encoding="utf-8")
    except Exception as e:
        log.error(f"Failed to read hosts file: {e}")
        return False

    # Check if any of the lines already exists
    already_present = []
    for line in lines:
        if line in content:
            already_present.append(line)

    if already_present:
        log.warning("The following entries already exist in hosts file:")
        for l in already_present:
            log.warning(f"  {l}")
        if len(already_present) == len(lines):
            log.info("No new entries to add.")
            return False

    # Backup before modification
    backup_hosts(hosts_path)

    # Append missing lines
    new_entries = [l for l in lines if l not in content]
    try:
        with open(hosts_path, "a", encoding="utf-8") as f:
            # Ensure there is a newline at the end before adding
            if content and not content.endswith("\n"):
                f.write("\n")
            for line in new_entries:
                f.write(line + "\n")
        log.info("Successfully added entries to hosts file.")
        return True
    except Exception as e:
        log.error(f"Failed to write to hosts file: {e}")
        return False

# ------------------------------
# Cache cleaning
# ------------------------------
def clear_cache():
    """Remove the TeamSpeak 3 cache directory if it exists."""
    cache_dir = get_cache_dir()
    if not cache_dir.exists():
        log.warning(f"Cache directory does not exist: {cache_dir}")
        return
    try:
        shutil.rmtree(cache_dir)
        log.info(f"Cache cleared successfully: {cache_dir}")
    except Exception as e:
        log.error(f"Failed to clear cache: {e}")

# ------------------------------
# Banner (topping)
# ------------------------------
def print_banner():
    """Display a colorful banner for the tool."""
    banner_text = """
  _______  ____   ____ _____  ____                       
 |__   __|/ __ \ / ____|  __ \|  _ \                      
    | |  | |  | | (___ | |__) | |_) |_   ___   _ _ __ ___ 
    | |  | |  | |\___ \|  ___/|  _ <| | | \ \ / / '_ ` _ \\
    | |  | |__| |____) | |    | |_) | |_| |\ V /| | | | | |
    |_|   \____/|_____/|_|    |____/ \__, | \_/ |_| |_| |_|
                                     __/ |                 
               Blacklist Bypass     |___/   & Cache Cleaner
    """
    print(COLOR_MAP['BANNER'] + banner_text + RESET)
    log.info("Welcome to TS3 Blacklist Bypass Tool")
    log.info("This tool modifies the system hosts file and clears TS3 cache.")
    log.warning("Requires administrator/root privileges.")

# ------------------------------
# Interactive menu
# ------------------------------
def main_menu():
    """Display the interactive menu and handle user choices."""
    while True:
        print("\n" + "="*60)
        print(COLOR_MAP['PROMPT'] + "  [1]  Add blacklist bypass entries to hosts" + RESET)
        print(COLOR_MAP['PROMPT'] + "  [2]  Clear TeamSpeak 3 cache" + RESET)
        print(COLOR_MAP['PROMPT'] + "  [3]  Exit" + RESET)
        print("="*60)
        try:
            choice = input(COLOR_MAP['PROMPT'] + "Enter your choice (1/2/3): " + RESET).strip()
        except (EOFError, KeyboardInterrupt):
            log.info("Exiting.")
            break

        if choice == "1":
            lines = [
                "0.0.0.0 blacklist2.teamspeak.com",
                "0.0.0.0 blacklist.teamspeak.com"
            ]
            hosts_path = get_hosts_path()
            log.info(f"Target hosts file: {hosts_path}")
            append_lines_to_hosts(hosts_path, lines)
        elif choice == "2":
            log.info("Clearing cache...")
            clear_cache()
        elif choice == "3":
            log.info("Goodbye!")
            break
        else:
            log.error("Invalid choice. Please enter 1, 2, or 3.")
        time.sleep(1.5)  # Brief pause to read messages

# ------------------------------
# Entry point
# ------------------------------
def main():
    """Main entry point of the application."""
    print_banner()
    
    if not is_admin():
        log.error("This script must be run with administrator/root privileges.")
        time.sleep(5)
        sys.exit(1)
    
    try:
        main_menu()
    except KeyboardInterrupt:
        log.info("Interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()