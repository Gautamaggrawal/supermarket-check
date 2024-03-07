import sys
from checkout import Checkout, PricingRule

def run_gui(pricing_rules):
    import tkinter as tk
    from supermarket_gui import GUI
    root = tk.Tk()
    checkout = Checkout(pricing_rules)
    gui = GUI(root, checkout, pricing_rules)
    gui.run()

def run_non_gui(pricing_rules):
    checkout = Checkout(pricing_rules)
    checkout.scan_item('')  # Will show a warning
    checkout.scan_item('A')
    checkout.scan_item('B')
    checkout.scan_item('B')
    checkout.scan_item('B')
    total = checkout.calculate_total()
    print("Total Price:", total)

def main():
    pricing_rules = {
        'A': PricingRule('A', 'discount', 50, 3, 130),
        'B': PricingRule('B', 'discount', 30, 2, 45),
        'C': PricingRule('C', 'individual', 20),
        'D': PricingRule('D', 'individual', 15),
        # Add more items with their pricing rules here if needed
    }

    if len(sys.argv) == 2 and sys.argv[1] == "gui":
        run_gui(pricing_rules)
    else:
        run_non_gui(pricing_rules)

if __name__ == "__main__":
    main()
