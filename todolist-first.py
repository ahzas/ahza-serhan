# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:04:05 2025

@author: AIRI
"""

print("To Do List Uygulamasına Hoş Geldiniz!")

tasks =[]

next_id = 1

def print_menu():
    print("\n--- Menu ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Tasks")
    print("4. Delete Tasks")
    print("5. Quit")
    
print_menu()


while True:
    print_menu()
    choice = input("Please Select 1-5: ").strip()
   
    if choice == "1":
    
        text = input("Enter a new task.\n").strip()
        if text == "":
            print("This field is required.\n")
            continue
        tasks.append({"id": next_id, "task": text, "done": False})
        print(f"Task added. (ID: {next_id}).")
        next_id += 1
        
    elif choice == "2":
        if not tasks:
            print("Any task not found.\n")
        else:
            print("ID | Done | Task")
            print("\n---|------------|--------------------")
            for t in tasks:
                durum = "✅" if t["done"] else "❌"
                print(f'{t["id"]:>2} | {durum}      | {t["task"]} ')
            
    elif choice == "3":
        raw = input("Task to be completed ID:")
        
        if not raw.isdigit():
            print("Please enter numerical value!")
            continue
        
        wanted_id = int(raw)
        
        found = False
        
        for t in tasks:
            
            if t["id"] == wanted_id:
                
                t["done"] = True
                
                found = True
                
                print(f"Task completed! (ID: {wanted_id}).")
                
                break
    
    elif choice == "4":
        
            raw = input("Enter the task ID to be deleted.").strip()
            
            if not raw.isdigit():
                
                print("Please enter numerical value!")
                
                continue
            
            wanted_id = int(raw)
        
            index = None
        
            for i, t in enumerate(tasks):
            
                if t["id"] == wanted_id:
                    
                    index = i
                    
                    break
            
            if index is None:
               
                print("No task found with this ID.\n")
                
            else: 
                
                removed = tasks.pop(index)
                
                print(f'Deleted: (ID: {removed["id"]})  {removed["task"]}')
                
    elif choice == "5":
        
        print("See you later :)")
        break
    
    else:
        
        print("! İnvalid value. Please enter a number between 1-5.")
    
                
            
   