#!/bin/bash

# Get the current date
current_date=$(date +"%Y-%m-%d")

# Update the date in the index.html file
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS version
    sed -i '' '/<p>.*Last time this was edited was.*<\/p>/c\
    <p>\
        Last time this was edited was '"$current_date"'.\
    </p>' index.html
else
    # Linux version
    sed -i '/<p>.*Last time this was edited was.*<\/p>/c\    <p>\n        Last time this was edited was '"$current_date"'.\n    </p>' index.html
fi

# Add all changes to git
git add .

# Commit changes with a message
git commit -m "Updated on $current_date"

# Push changes to the remote repository
git push

echo "Changes have been committed and pushed. Date updated to $current_date in index.html"