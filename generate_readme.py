#!/usr/bin/env python3
"""
Generate README.md from workflows.json
"""

import json
import os

def generate_readme():
    # Load workflows data
    with open('workflows.json', 'r') as f:
        workflows = json.load(f)
    
    # Generate README content
    readme_content = """# N8N Workflows Index

"""
    
    # Add each workflow
    for workflow in workflows:
        repo_name = workflow['repo_link'].split('/')[-1]
        readme_content += f"## {repo_name}\n\n"
        readme_content += f"{workflow['description']}\n\n"
        readme_content += f"[![Repository](https://img.shields.io/badge/Repository-{repo_name}-blue?style=for-the-badge&logo=github)]({workflow['repo_link']})\n\n"
        readme_content += "---\n\n"
    
    # Add footer
    readme_content += """ 
- [N8N Creator Profile](https://n8n.io/creators/danielrosehill/)

"""
    
    # Write README
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
