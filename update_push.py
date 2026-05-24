#!/usr/bin/env python3
import os
import subprocess
from datetime import date

def update_html():
    # Get current date in both formats
    current_date = date.today().strftime("%Y-%m-%d")
    
    # Read the content of index.html
    with open('index.html', 'r') as file:
        content = file.readlines()
    
    # Update last-updated timestamp
    for i, line in enumerate(content):
        if "Last updated:" in line:
            content[i] = f"    <small style=\"position:fixed;bottom:10px;left:12px;font-size:11px;opacity:0.4;pointer-events:none;\">Last updated: {current_date}</small>\n"
    
    # Write the updated content back to index.html
    with open('index.html', 'w') as file:
        file.writelines(content)
    
    return current_date

def git_operations(date):
    commands = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', f"Updated on {date}"],
        ['git', 'push']
    ]
    
    for cmd in commands:
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    current_date = update_html()
    git_operations(current_date)
    print(f"Changes have been committed and pushed. Date updated to {current_date} in index.html")