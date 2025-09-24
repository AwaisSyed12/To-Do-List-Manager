"""
To-Do List Application
======================
A simple console-based to-do list manager with persistent storage
Author: Awais Syed
Email: awaissyed1212@gmail.com
Features: Add, Remove, View tasks with file-based persistence
"""

import os
from datetime import datetime
from typing import List, Optional

class TodoManager:
    
    def __init__(self, filename: str = "tasks.txt"):
        self.filename = filename
        self.tasks: List[dict] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.strip()
                        if line: 
                            parts = line.split('|')
                            if len(parts) >= 4:
                                task = {
                                    'id': int(parts[0]),
                                    'task': parts[1],
                                    'status': parts[2],
                                    'date_added': parts[3]
                                }
                                self.tasks.append(task)
                print(f"✅ Loaded {len(self.tasks)} tasks from {self.filename}")
            else:
                print(f"📝 No existing tasks file found. Creating new task list.")
        except Exception as e:
            print(f"⚠️ Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self) -> None:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for task in self.tasks:
                    line = f"{task['id']}|{task['task']}|{task['status']}|{task['date_added']}\n"
                    file.write(line)
            print(f"💾 Tasks saved to {self.filename}")
        except Exception as e:
            print(f"⚠️ Error saving tasks: {e}")
    
    def get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def add_task(self, task_description: str) -> None:
        if not task_description.strip():
            print("⚠️ Task description cannot be empty!")
            return
        
        new_task = {
            'id': self.get_next_id(),
            'task': task_description.strip(),
            'status': 'Pending',
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Task added successfully! (ID: {new_task['id']})")
    
    def remove_task(self, task_id: int) -> None:
        task_to_remove = None
        for task in self.tasks:
            if task['id'] == task_id:
                task_to_remove = task
                break
        
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.save_tasks()
            print(f"✅ Task {task_id} removed successfully!")
        else:
            print(f"⚠️ Task with ID {task_id} not found!")
    
    def mark_complete(self, task_id: int) -> None:
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                self.save_tasks()
                print(f"✅ Task {task_id} marked as completed!")
                return
        print(f"⚠️ Task with ID {task_id} not found!")
    
    def view_tasks(self, show_completed: bool = True) -> None:
        if not self.tasks:
            print("📝 No tasks found! Your to-do list is empty.")
            return
        
        display_tasks = self.tasks
        if not show_completed:
            display_tasks = [task for task in self.tasks if task['status'] != 'Completed']
        
        if not display_tasks:
            print("📝 No pending tasks found!")
            return
        
        print("\n" + "="*80)
        print("                           📝 TO-DO LIST")
        print("="*80)
        print(f"{'ID':<4} {'Task':<40} {'Status':<12} {'Date Added':<20}")
        print("-"*80)
        
        for task in display_tasks:
            status_icon = "✅" if task['status'] == 'Completed' else "⏳"
            print(f"{task['id']:<4} {task['task'][:40]:<40} {status_icon} {task['status']:<10} {task['date_added']:<20}")
        
        print("-"*80)
        pending_count = sum(1 for task in self.tasks if task['status'] == 'Pending')
        completed_count = sum(1 for task in self.tasks if task['status'] == 'Completed')
        print(f"📊 Total: {len(self.tasks)} | Pending: {pending_count} | Completed: {completed_count}")
        print("="*80)
    
    def search_tasks(self, keyword: str) -> None:
        if not keyword.strip():
            print("⚠️ Search keyword cannot be empty!")
            return
        
        matching_tasks = [task for task in self.tasks if keyword.lower() in task['task'].lower()]
        
        if not matching_tasks:
            print(f"🔍 No tasks found containing '{keyword}'")
            return
        
        print(f"\n🔍 Search results for '{keyword}':")
        print("-"*50)
        for task in matching_tasks:
            status_icon = "✅" if task['status'] == 'Completed' else "⏳"
            print(f"ID {task['id']}: {task['task']} [{status_icon} {task['status']}]")

def display_menu() -> None:
    print("\n" + "="*60)
    print("           📝 TO-DO LIST MANAGER")
    print("="*60)
    print("1. 📝 Add Task")
    print("2. 👀 View All Tasks") 
    print("3. 👁️ View Pending Tasks Only")
    print("4. ✅ Mark Task as Complete")
    print("5. 🗑️ Remove Task")
    print("6. 🔍 Search Tasks")
    print("7. 📊 Show Statistics")
    print("8. 🚪 Exit")
    print("-"*60)

def get_user_choice() -> int:
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("⚠️ Please enter a number between 1 and 8.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def show_statistics(todo_manager: TodoManager) -> None:
    if not todo_manager.tasks:
        print("📊 No tasks to analyze!")
        return
    
    total_tasks = len(todo_manager.tasks)
    pending_tasks = sum(1 for task in todo_manager.tasks if task['status'] == 'Pending')
    completed_tasks = sum(1 for task in todo_manager.tasks if task['status'] == 'Completed')
    completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    print("\n" + "="*50)
    print("           📊 TASK STATISTICS")
    print("="*50)
    print(f"📝 Total Tasks: {total_tasks}")
    print(f"⏳ Pending Tasks: {pending_tasks}")
    print(f"✅ Completed Tasks: {completed_tasks}")
    print(f"📈 Completion Rate: {completion_rate:.1f}%")
    print("="*50)

def main():
    print("🎉 Welcome to Your Personal To-Do List Manager! 🎉")
    print("Stay organized and productive with persistent task management.")
    
    todo_manager = TodoManager()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            print("\n📝 Adding New Task")
            task = input("Enter task description: ").strip()
            todo_manager.add_task(task)
        
        elif choice == 2:
            todo_manager.view_tasks(show_completed=True)
        
        elif choice == 3:
            todo_manager.view_tasks(show_completed=False)
        
        elif choice == 4:
            todo_manager.view_tasks(show_completed=False)
            if todo_manager.tasks:
                try:
                    task_id = int(input("\nEnter task ID to mark as complete: "))
                    todo_manager.mark_complete(task_id)
                except ValueError:
                    print("⚠️ Please enter a valid task ID number.")
        
        elif choice == 5:
            todo_manager.view_tasks()
            if todo_manager.tasks:
                try:
                    task_id = int(input("\nEnter task ID to remove: "))
                    confirm = input(f"Are you sure you want to remove task {task_id}? (y/n): ").lower()
                    if confirm in ['y', 'yes']:
                        todo_manager.remove_task(task_id)
                    else:
                        print("❌ Task removal cancelled.")
                except ValueError:
                    print("⚠️ Please enter a valid task ID number.")
        
        elif choice == 6:
            keyword = input("\n🔍 Enter search keyword: ").strip()
            todo_manager.search_tasks(keyword)
        
        elif choice == 7:
            show_statistics(todo_manager)
        
        elif choice == 8:
            print("\n💾 Saving your tasks...")
            todo_manager.save_tasks()
            print("✨ Thank you for using To-Do List Manager!")
            print("Stay productive! 🚀")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
