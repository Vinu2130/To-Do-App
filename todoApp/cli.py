# This file handles the command-line interface.

import argparse                                                                                 # for parsing command-line arguments
from todoApp import add_task, remove_task, list_tasks , mark_done, mark_undone             # Imports functions from todo.py.

def cli_main(args=None):
    parser = argparse.ArgumentParser("ToDo List CLI")                                           # Creates an argument parser with a description.
    subparsers = parser.add_subparsers(dest = "command")                                        # Adds subparsers for different commands.

    # add task
    add_parser = subparsers.add_parser("add",help = "to add a new task")                        # Adds a parser for the add command.
    add_parser.add_argument("task",help ="the task to add")                                     # Adds a positional argument for the task description.
    
    # remove task
    remove_parser = subparsers.add_parser("remove",help = "to add a new task")                  # Adds a parser for the remove command.
    remove_parser.add_argument("task_number",type=int,help ="the task number to remove")        

    # list task
    list_parser = subparsers.add_parser("list", help = "to list all tasks")                     # Adds a parser for the list command

    # Mark done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_number", type=int, help="The task number to mark as done")   # Adds a parser for the Mark done command

    # Mark undone command
    undone_parser = subparsers.add_parser("undone", help="Mark a task as not done")             # Adds a parser for the Mark undone command
    undone_parser.add_argument("task_number", type=int, help="The task number to mark as not done")

    # Clear tasks command
    # clear_parser = subparsers.add_parser('clear', help='Clear all tasks')

    # Help command
    help_parser = subparsers.add_parser("help", help="Show help message")
    
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.task_number)
    elif args.command == "undone":
        mark_undone(args.task_number)
    elif args.command == "remove":
        remove_task(args.task_number)
    # elif args.command == 'clear':
    #     clear_tasks()
    elif args.command == "help" or args.command is None:
        parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    cli_main()
    
