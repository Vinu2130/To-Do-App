import sys
import tkinter as tk
from tkinter import messagebox
from todoApp.cli import cli_main
from todoApp.gui import main as gui_main

def main():
    if len(sys.argv) > 1:
        # Pass arguments to the CLI main function
        cli_main(sys.argv[1:])
    else:
        print("Welcome to the To-Do List Application!")
        print("Choose your preferred interface:")
        print("1. CLI (Command Line Interface)")
        print("2. GUI (Graphical User Interface)")
        choice = input("Enter 1 or 2: ").strip()

        if choice == '1':
            cli_main()
        elif choice == '2':
            gui_main()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
