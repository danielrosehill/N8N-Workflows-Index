#!/usr/bin/env python3
"""
N8N Workflows Index Management CLI
"""

import json
import sys
from datetime import datetime
import urllib.parse

def load_workflows():
    """Load workflows from JSON file"""
    try:
        with open('workflows.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_workflows(workflows):
    """Save workflows to JSON file"""
    with open('workflows.json', 'w') as f:
        json.dump(workflows, f, indent=2)

def list_workflows():
    """List all workflows"""
    workflows = load_workflows()
    if not workflows:
        print("No workflows found.")
        return
    
    print(f"\n{'#':<3} {'Title':<40} {'Date Added':<12}")
    print("-" * 60)
    for i, workflow in enumerate(workflows, 1):
        title = workflow.get('title', 'N/A')[:38]
        date_added = workflow.get('date_added', 'N/A')
        print(f"{i:<3} {title:<40} {date_added:<12}")
    print()

def add_workflow():
    """Add a new workflow"""
    print("\n=== Add New Workflow ===")
    
    title = input("Enter workflow title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    
    repo_link = input("Enter repository URL: ").strip()
    if not repo_link:
        print("Repository URL cannot be empty!")
        return
    
    if not repo_link.startswith('https://github.com/'):
        print("Repository URL must be a GitHub URL!")
        return
    
    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty!")
        return
    
    # Get current date
    date_added = datetime.now().strftime('%Y-%m-%d')
    
    # Create new workflow entry
    new_workflow = {
        "title": title,
        "repo_link": repo_link,
        "description": description,
        "date_added": date_added
    }
    
    # Load existing workflows and add new one
    workflows = load_workflows()
    workflows.append(new_workflow)
    
    # Save updated workflows
    save_workflows(workflows)
    
    print(f"\n✅ Workflow '{title}' added successfully!")
    print(f"   Date: {date_added}")
    print(f"   Repository: {repo_link}")
    print(f"   Description: {description}")

def remove_workflow():
    """Remove a workflow"""
    workflows = load_workflows()
    if not workflows:
        print("No workflows to remove.")
        return
    
    list_workflows()
    
    try:
        index = int(input("Enter workflow number to remove: ")) - 1
        if 0 <= index < len(workflows):
            removed = workflows.pop(index)
            save_workflows(workflows)
            print(f"\n✅ Workflow '{removed['title']}' removed successfully!")
        else:
            print("Invalid workflow number!")
    except ValueError:
        print("Please enter a valid number!")

def edit_workflow():
    """Edit an existing workflow"""
    workflows = load_workflows()
    if not workflows:
        print("No workflows to edit.")
        return
    
    list_workflows()
    
    try:
        index = int(input("Enter workflow number to edit: ")) - 1
        if 0 <= index < len(workflows):
            workflow = workflows[index]
            print(f"\nEditing: {workflow['title']}")
            print("(Press Enter to keep current value)")
            
            new_title = input(f"Title [{workflow['title']}]: ").strip()
            if new_title:
                workflow['title'] = new_title
            
            new_repo = input(f"Repository [{workflow['repo_link']}]: ").strip()
            if new_repo:
                if new_repo.startswith('https://github.com/'):
                    workflow['repo_link'] = new_repo
                else:
                    print("Repository URL must be a GitHub URL! Keeping original.")
            
            new_desc = input(f"Description [{workflow['description']}]: ").strip()
            if new_desc:
                workflow['description'] = new_desc
            
            save_workflows(workflows)
            print(f"\n✅ Workflow updated successfully!")
        else:
            print("Invalid workflow number!")
    except ValueError:
        print("Please enter a valid number!")

def regenerate_readme():
    """Regenerate README from workflows.json"""
    try:
        import subprocess
        result = subprocess.run(['python3', 'generate_readme.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ README regenerated successfully!")
        else:
            print(f"❌ Error regenerating README: {result.stderr}")
    except Exception as e:
        print(f"❌ Error running generate_readme.py: {e}")

def show_menu():
    """Show main menu"""
    print("\n=== N8N Workflows Index Manager ===")
    print("1. List workflows")
    print("2. Add workflow")
    print("3. Edit workflow")
    print("4. Remove workflow")
    print("5. Regenerate README")
    print("6. Exit")
    print()

def main():
    """Main CLI loop"""
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            list_workflows()
        elif choice == '2':
            add_workflow()
        elif choice == '3':
            edit_workflow()
        elif choice == '4':
            remove_workflow()
        elif choice == '5':
            regenerate_readme()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
