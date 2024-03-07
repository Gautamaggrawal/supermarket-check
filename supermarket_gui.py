import tkinter as tk
from tkinter import messagebox
from checkout import PricingRule

class GUI:
    def __init__(self, root, checkout, pricing_rules):
        self.root = root
        self.checkout = checkout
        self.pricing_rules = pricing_rules

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Scan items:").pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        tk.Button(self.root, text="Scan", command=self.scan_item).pack()

        self.total_label = tk.Label(self.root, text="Total: Rs 0")
        self.total_label.pack()

        tk.Button(self.root, text="Add Rule", command=self.add_rule_window).pack()
        tk.Button(self.root, text="Display Rules", command=self.display_rules).pack()

        self.rules_text = tk.Text(self.root, height=10, width=90)
        self.rules_text.pack()
        self.display_rules()

    def scan_item(self):
        items = self.entry.get().upper()
        for item in items:
            self.checkout.scan_item(item)
        self.update_total()
        self.entry.delete(0, tk.END)

    def update_total(self):
        try:
            total_price = self.checkout.calculate_total()
            self.total_label.config(text=f"Total: Rs {total_price}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def add_rule_window(self):
        add_rule_window = tk.Toplevel(self.root)
        add_rule_window.title("Add Pricing Rule")

        tk.Label(add_rule_window, text="Item:").grid(row=0, column=0)
        self.item_entry = tk.Entry(add_rule_window)
        self.item_entry.grid(row=0, column=1)

        tk.Label(add_rule_window, text="Price:").grid(row=1, column=0)
        self.price_entry = tk.Entry(add_rule_window)
        self.price_entry.grid(row=1, column=1)

        tk.Label(add_rule_window, text="Rule Type:").grid(row=2, column=0)
        self.rule_type_var = tk.StringVar()
        self.rule_type_var.set("individual")
        tk.Radiobutton(add_rule_window, text="Individual", variable=self.rule_type_var, value="individual").grid(row=2, column=1)
        tk.Radiobutton(add_rule_window, text="Discount", variable=self.rule_type_var, value="discount").grid(row=2, column=2)

        tk.Label(add_rule_window, text="Quantity (for discount):").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(add_rule_window)
        self.quantity_entry.grid(row=3, column=1)

        tk.Label(add_rule_window, text="Discounted Price:").grid(row=4, column=0)
        self.discounted_price_entry = tk.Entry(add_rule_window)
        self.discounted_price_entry.grid(row=4, column=1)

        tk.Button(add_rule_window, text="Add Rule", command=self.add_rule).grid(row=5, column=0, columnspan=2)

    def add_rule(self):
        item = self.item_entry.get()
        price = float(self.price_entry.get())
        rule_type = self.rule_type_var.get()
        quantity = int(self.quantity_entry.get()) if self.rule_type_var.get() == "discount" else None
        discounted_price = float(self.discounted_price_entry.get()) if self.rule_type_var.get() == "discount" else None

        if item in self.pricing_rules:
            messagebox.showwarning("Existing Item", f"Pricing rule already exists for item {item}.")
        else:
            self.pricing_rules[item] = PricingRule(item, rule_type, price, quantity, discounted_price)
            messagebox.showinfo("Rule Added", f"Pricing rule added for item {item}.")
            self.display_rules()
    
    def display_rules(self):
        self.rules_text.delete(1.0, tk.END)  
        if self.pricing_rules:
            for item, rule in self.pricing_rules.items():
                self.rules_text.insert(tk.END, f"Item: {item}, Rule: {rule}\n")
        else:
            self.rules_text.insert(tk.END, "No pricing rules added yet.")
    
    def run(self):
        self.root.mainloop()
