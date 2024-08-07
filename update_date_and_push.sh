#!/bin/bash

# Get the current date
current_date=$(date +"%Y-%m-%d")

# Update the date in the index.html file
awk -v date="$current_date" '
/<p>.*Last time this was edited was.*<\/p>/ {
    print "    <p>"
    print "        Last time this was edited was " date "."
    print "    </p>"
    next
}
{print}' index.html > temp.html && mv temp.html index.html

# Add all changes to git
git add .

# Commit changes with a message
git commit -m "Updated on $current_date"

# Push changes to the remote repository
git push

echo "Changes have been committed and pushed. Date updated to $current_date in index.html"