#!/usr/bin/env python3
import os
import subprocess
from datetime import date

def update_html():
    # Get current date in both formats
    current_date = date.today().strftime("%Y-%m-%d")
    # Convert to Japanese format (YYYY年MM月DD日)
    japanese_date = date.today().strftime("%Y年%m月%d日")
    
    # Read the content of index.html
    with open('index.html', 'r') as file:
        content = file.readlines()
    
    # Update both English and Japanese dates
    for i, line in enumerate(content):
        if "Last time this was edited was" in line:
            content[i] = f"        <p lang=\"en\">Last time this was edited was {current_date} (YYYY/MM/DD).</p>\n"
        elif "最終更新日：" in line:
            content[i] = f"        <p lang=\"ja\">最終更新日：{japanese_date}</p>\n"
    
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