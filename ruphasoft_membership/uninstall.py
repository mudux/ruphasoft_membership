import os


def before_uninstall():
    print("Before Uninstall")
    print("=====================================")
    print("removing icons from icons.svg")
    os.remove("/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
    os.rename("/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.bak.svg", "/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
    print("=====================================")
    print("Before Uninstall DONE!")