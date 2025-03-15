import tkinter as tk
from tkinter import messagebox

# Set to store blocked IP addresses
blocked_ips = set()

def block_ip():
    """Block an IP address and log the action."""
    ip = ip_entry.get().strip()
    if ip:
        blocked_ips.add(ip)
        log_activity(f"Blocked IP: {ip}")
        update_blocked_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")

def unblock_ip():
    """Unblock an IP address and log the action."""
    ip = ip_entry.get().strip()
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        log_activity(f"Unblocked IP: {ip}")
        update_blocked_list()
    else:
        messagebox.showwarning("Input Error", "IP not found in blocked list.")

def update_blocked_list():
    """Update the listbox showing blocked IPs."""
    blocked_list.delete(0, tk.END)
    for ip in blocked_ips:
        blocked_list.insert(tk.END, ip)

def log_activity(activity):
    """Log firewall activities to a file."""
    with open("firewall_log.txt", "a") as log_file:
        log_file.write(activity + "\n")

def check_ip():
    """Check if an IP is blocked or allowed."""
    ip = ip_entry.get().strip()
    if ip in blocked_ips:
        messagebox.showerror("Access Denied", f"Access Denied: {ip} is blocked.")
    else:
        messagebox.showinfo("Access Granted", f"Access Granted: {ip} is allowed.")

# GUI Setup
root = tk.Tk()
root.title("Simple Firewall")

# Input field
tk.Label(root, text="Enter IP Address:").pack(pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Block IP", command=block_ip).pack(pady=5)
tk.Button(root, text="Unblock IP", command=unblock_ip).pack(pady=5)
tk.Button(root, text="Check IP", command=check_ip).pack(pady=5)

# Blocked IPs List
tk.Label(root, text="Blocked IPs:").pack(pady=5)
blocked_list = tk.Listbox(root, width=30, height=10)
blocked_list.pack(pady=5)

root.mainloop()