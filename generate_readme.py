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
        title = workflow.get('title', workflow['repo_link'].split('/')[-1])
        date_added = workflow.get('date_added', 'N/A')
        repo_name = workflow['repo_link'].split('/')[-1]
        
        readme_content += f"## {title}\n\n"
        readme_content += f"{workflow['description']}\n\n"
        readme_content += f"*Added: {date_added}*\n\n"
        
        # Create a simple repository link instead of badge for now
        readme_content += f"[📂 Repository]({workflow['repo_link']})\n\n"
        readme_content += "---\n\n"
    
    # Add N8N section
    readme_content += """## N8N

https://n8n.io/workflows/4197-improve-ai-agent-system-prompts-with-gpt-4o-feedback-analysis-and-email-delivery/

 
- [N8N Creator Profile](https://n8n.io/creators/danielrosehill/)

"""
    
    # Write README
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
