#!/usr/bin/env python3

import tkinter as tk
import os

class Main:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("System GUI")
        pa = __file__.split("/")
        self.root.iconbitmap("/".join(pa[:len(pa) - 1]) + "/icon.ico")
        self.root.geometry("365x320")

        self.root.columnconfigure(1, weight = 5)
        self.root.rowconfigure(0, weight = 3)
        self.root.rowconfigure(2, weight = 2)

        self.inp_text = tk.Text(self.root)
        self.inp_scroll = tk.Scrollbar(self.root, command = self.inp_text.yview)
        self.inp_text.configure(yscrollcommand = self.inp_scroll.set)
        self.inp_text.grid(sticky = "we", padx = 3, pady = 3, row = 0, column = 0, columnspan = 2)
        self.inp_scroll.grid(sticky = "ns", row = 0, column = 2)

        self.submit_button = tk.Button(self.root, text = "run", command = self.sys_cb)
        self.submit_button.grid(row = 1, column = 0)

        self.out_text = tk.Text(self.root, height = 15, state = tk.DISABLED)
        self.out_scroll = tk.Scrollbar(self.root, command = self.out_text.yview)
        self.out_text.configure(yscrollcommand = self.out_scroll.set)
        self.out_text.grid(sticky = "we", padx = 3, pady = 3, row = 2, column = 0, columnspan = 2)
        self.out_scroll.grid(sticky = "ns", row = 2, column = 2)

    def run(self) -> None:
        self.root.mainloop()

    def sys_cb(self) -> None:
        inp = self.inp_text.get("1.0", tk.END)
        p = os.popen(inp)
        res = p.read()
        ret = p.close()
        self.out_text.config(state = tk.NORMAL)
        self.out_text.delete("1.0", tk.END)
        if ret == None:
            self.out_text.insert("1.0", res)
        else:
            self.out_text.insert("1.0", "unable to execute: " + inp)
        self.out_text.config(state = tk.DISABLED)

if __name__ == "__main__":
    main = Main()
    main.run()