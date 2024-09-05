import os
import psutil
import subprocess

def detect_drive():
    # Get all mounted partitions
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        if 'removable' in partition.opts:
            return partition.device  # Return the first removable drive found
    return None

def repair_drive(drive):
    try:
        print(f"Running chkdsk on {drive}...")
        # Running chkdsk to check and repair the drive
        result = subprocess.run(['chkdsk', drive, '/f'], capture_output=True, text=True)
        print(result.stdout)
        
        if result.returncode == 0:
            print(f"{drive} has been repaired successfully!")
        else:
            print(f"An error occurred while repairing {drive}.")
    
    except Exception as e:
        print(f"Failed to run chkdsk: {e}")

if __name__ == "__main__":
    drive = detect_drive()
    
    if drive:
        print(f"Detected external drive: {drive}")
        repair_drive(drive)
    else:
        print("No external drive detected.")
