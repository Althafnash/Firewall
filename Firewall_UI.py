import tkinter as tk
from tkinter import scrolledtext
from Firewall import Firewall

class NashFirewallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nash_Firewall -- Firewall")
        self.root.geometry("750x550")

        self.firewall = Firewall(self.output_callback)

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Nash Firewall").grid(row=1, column=0, padx=75, pady=10)
        tk.Label(self.root, text="The Firewall scan can be seen below. Click start to start the Firewall and click the stop button to stop the firewall").grid(row=2, column=0, padx=75, pady=10)

        self.terminal = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.terminal.grid(row=3, column=0, padx=10, pady=10)
        self.terminal.insert(tk.END, "Welcome to Nash Firewall Terminal\n")
        self.terminal.config(state=tk.DISABLED)

        start_button = tk.Button(self.root, text="Start Firewall", command=self.start_firewall)
        start_button.grid(row=4, column=0, padx=2, pady=2)

        stop_button = tk.Button(self.root, text="Stop Firewall", command=self.stop_firewall)
        stop_button.grid(row=5, column=0, padx=2, pady=2)

        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def start_firewall(self):
        self.firewall.start_firewall("eth0")  # Replace "eth0" with the appropriate interface

    def stop_firewall(self):
        self.firewall.stop_firewall()

    def output_callback(self, message):
        self.terminal.config(state=tk.NORMAL)
        self.terminal.insert(tk.END, message)
        self.terminal.see(tk.END)
        self.terminal.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NashFirewallApp(root)
    root.mainloop()
