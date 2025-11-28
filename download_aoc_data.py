#!/usr/bin/env python3
import os
import requests
from pathlib import Path
import time

def download_aoc_data(session_cookie):
    base_url = "https://adventofcode.com/{year}/day/{day}/input"
    data_dir = Path("data")
    
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "AoC Data Downloader (github.com/username/repo)"
    }
    
    years = range(2015, 2025)
    days = range(1, 26)
    
    for year in years:
        year_dir = data_dir / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)
        
        for day in days:
            filename = year_dir / f"day_{day:02d}.data"
            
            if filename.exists():
                print(f"Skipping {year} day {day} - already exists")
                continue
            
            url = base_url.format(year=year, day=day)
            print(f"Downloading {year} day {day}...")
            
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    with open(filename, 'w') as f:
                        f.write(response.text.rstrip('\n'))
                    print(f"  ✓ Saved to {filename}")
                elif response.status_code == 404:
                    print(f"  ✗ Day {day} not available yet")
                    break
                else:
                    print(f"  ✗ Error {response.status_code}: {response.text[:100]}")
                    if response.status_code == 400:
                        print("Session cookie might be invalid. Please check your session.")
                        return
            except Exception as e:
                print(f"  ✗ Error downloading: {e}")
            
            time.sleep(0.5)

if __name__ == "__main__":
    session_cookie = input("Please enter your AoC session cookie: ").strip()
    
    if not session_cookie:
        print("Session cookie is required. You can find it in your browser's cookies for adventofcode.com")
        exit(1)
    
    download_aoc_data(session_cookie)
    print("\nDownload complete!")