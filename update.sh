#!/bin/bash
# Update README from workflows.json

echo "Generating README from workflows.json..."
python3 generate_readme.py

echo "README updated successfully!"
echo ""
echo "To commit changes:"
echo "git add ."
echo "git commit -m 'Update workflows index'"
echo "git push"
