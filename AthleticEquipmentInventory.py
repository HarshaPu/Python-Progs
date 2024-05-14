import datetime
import tkinter as tk
from tkinter import ttk, messagebox
class Equipment:
    def __init__(self, equipment_id, name, quantity, condition):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.last_used = None
        self.replacement_date = None

    def __str__(self):
        return f"ID: {self.equipment_id}, Name: {self.name}, Quantity: {self.quantity}, Condition: {self.condition}, Last Used: {self.last_used}"

    def update_last_used_date(self):
        self.last_used = datetime.datetime.now()

    def to_dict(self):
        return {
            'equipment_id': self.equipment_id,
            'name': self.name,
            'quantity': self.quantity,
            'condition': self.condition,
            'last_used': str(self.last_used),
            'replacement_date': self.replacement_date
        }

    @staticmethod
    def from_dict(data):
        equipment = Equipment(data['equipment_id'], data['name'], data['quantity'], data['condition'])
        equipment.last_used = datetime.datetime.strptime(data['last_used'], "%Y-%m-%d %H:%M:%S.%f")
        equipment.replacement_date = data['replacement_date']
        return equipment

class EquipmentManager:
    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        for existing_equipment in self.equipment_list:
            if existing_equipment.equipment_id == equipment.equipment_id:
                messagebox.showerror("Error", "Equipment ID already exists.")
                return False
        self.equipment_list.append(equipment)
        self.save_to_file()  
        messagebox.showinfo("Success", "Equipment added successfully.")
        return True

    def update_equipment(self, equipment_id, **kwargs):
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                for key, value in kwargs.items():
                    setattr(equipment, key, value)
                self.save_to_file()  
                messagebox.showinfo("Success", "Equipment updated successfully.")
                return True
        messagebox.showerror("Error", "Equipment with given ID not found.")
        return False

    def delete_equipment(self, equipment_id):
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                self.equipment_list.remove(equipment)
                self.save_to_file()  # Save to file after deleting equipment
                messagebox.showinfo("Success", "Equipment removed successfully.")
                return True
        messagebox.showerror("Error", "Equipment with given ID not found.")
        return False

    def get_equipment_by_id(self, equipment_id):
        found = False
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                messagebox.showinfo("Equipment Details", str(equipment))
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Equipment Not Found")

    def get_all_equipment(self):
        equipment_details = '\n'.join(str(equipment) for equipment in self.equipment_list)
        messagebox.showinfo("All Equipment Details", equipment_details)

    def schedule_equipment_replacement(self, equipment_id, replacement_date):
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                equipment.replacement_date = replacement_date
                equipment.update_last_used_date()
                self.save_to_file()  # Save to file after scheduling replacement
                messagebox.showinfo("Success", f"Replacement scheduled for equipment id {equipment_id} on {replacement_date}.")
                messagebox.showinfo("Equipment Details after Replacement Schedule", str(equipment))
                return
        messagebox.showerror("Error", f"Equipment with ID {equipment_id} not found.")

    def save_to_file(self):
        with open("AthleticEquipmentData.txt", "w") as file:
            for equipment in self.equipment_list:
                file.write(str(equipment) + '\n')

    
manager = EquipmentManager()

def add_equipment():
    equipment_id = entry_id.get()
    name = entry_name.get()
    quantity = int(entry_quantity.get())
    condition = entry_condition.get()
    equipment = Equipment(equipment_id, name, quantity, condition)
    added = manager.add_equipment(equipment)
    reset_entry_fields()

def remove_equipment():
    equipment_id = entry_remove_id.get()
    manager.delete_equipment(equipment_id)
    reset_entry_fields()

def update_equipment():
    equipment_id = entry_update_id.get()
    new_quantity = int(entry_new_quantity.get())
    new_condition = entry_new_condition.get()
    manager.update_equipment(equipment_id, quantity=new_quantity, condition=new_condition)
    reset_entry_fields()

def display_equipment_by_id():
    equipment_id = entry_display_id.get()
    manager.get_equipment_by_id(equipment_id)

def display_all_equipment():
    manager.get_all_equipment()

def schedule_replacement():
    equipment_id = entry_schedule_id.get()
    replacement_date = entry_replacement_date.get()
    manager.schedule_equipment_replacement(equipment_id, replacement_date)
    reset_entry_fields()

def reset_entry_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_condition.delete(0, tk.END)
    entry_remove_id.delete(0, tk.END)
    entry_update_id.delete(0, tk.END)
    entry_new_quantity.delete(0, tk.END)
    entry_new_condition.delete(0, tk.END)
    entry_display_id.delete(0, tk.END)
    entry_schedule_id.delete(0, tk.END)
    entry_replacement_date.delete(0, tk.END)

root = tk.Tk()
root.title("Athletic Equipment Inventory")

# Create a Notebook (Tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Add Equipment
frame_add = ttk.Frame(notebook)
notebook.add(frame_add, text='Add Equipment')

label_id = tk.Label(frame_add, text="Equipment ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_add)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_name = tk.Label(frame_add, text="Equipment Name:")
label_name.grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_add)
entry_name.grid(row=1, column=1, padx=5, pady=5)

label_quantity = tk.Label(frame_add, text="Quantity:")
label_quantity.grid(row=2, column=0, padx=5, pady=5)
entry_quantity = tk.Entry(frame_add)
entry_quantity.grid(row=2, column=1, padx=5, pady=5)

label_condition = tk.Label(frame_add, text="Condition:")
label_condition.grid(row=3, column=0, padx=5, pady=5)
entry_condition = tk.Entry(frame_add)
entry_condition.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(frame_add, text="Add Equipment", command=add_equipment)
button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Remove Equipment
frame_remove = ttk.Frame(notebook)
notebook.add(frame_remove, text='Remove Equipment')

label_remove_id = tk.Label(frame_remove, text="Equipment ID to remove:")
label_remove_id.grid(row=0, column=0, padx=5, pady=5)
entry_remove_id = tk.Entry(frame_remove)
entry_remove_id.grid(row=0, column=1, padx=5, pady=5)

button_remove = tk.Button(frame_remove, text="Remove Equipment", command=remove_equipment)
button_remove.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Update Equipment
frame_update = ttk.Frame(notebook)
notebook.add(frame_update, text='Update Equipment')

label_update_id = tk.Label(frame_update, text="Equipment ID to update:")
label_update_id.grid(row=0, column=0, padx=5, pady=5)
entry_update_id = tk.Entry(frame_update)
entry_update_id.grid(row=0, column=1, padx=5, pady=5)

label_new_quantity = tk.Label(frame_update, text="New Quantity:")
label_new_quantity.grid(row=1, column=0, padx=5, pady=5)
entry_new_quantity = tk.Entry(frame_update)
entry_new_quantity.grid(row=1, column=1, padx=5, pady=5)

label_new_condition = tk.Label(frame_update, text="New Condition:")
label_new_condition.grid(row=2, column=0, padx=5, pady=5)
entry_new_condition = tk.Entry(frame_update)
entry_new_condition.grid(row=2, column=1, padx=5, pady=5)

button_update = tk.Button(frame_update, text="Update Equipment", command=update_equipment)
button_update.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Display Equipment By ID
frame_display_id = ttk.Frame(notebook)
notebook.add(frame_display_id, text='Display Equipment By ID')

label_display_id = tk.Label(frame_display_id, text="Enter equipment ID:")
label_display_id.grid(row=0, column=0, padx=5, pady=5)
entry_display_id = tk.Entry(frame_display_id)
entry_display_id.grid(row=0, column=1, padx=5, pady=5)

button_display_id = tk.Button(frame_display_id, text="Display Equipment", command=display_equipment_by_id)
button_display_id.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Display All Equipment
frame_display_all = ttk.Frame(notebook)
notebook.add(frame_display_all, text='Display All Equipment')

button_display_all = tk.Button(frame_display_all, text="Display All Equipment", command=display_all_equipment)
button_display_all.pack(padx=5, pady=5)

# Schedule Replacement
frame_schedule = ttk.Frame(notebook)
notebook.add(frame_schedule, text='Schedule Replacement')

label_schedule_id = tk.Label(frame_schedule, text="Equipment ID For Replacement:")
label_schedule_id.grid(row=0, column=0, padx=5, pady=5)
entry_schedule_id = tk.Entry(frame_schedule)
entry_schedule_id.grid(row=0, column=1, padx=5, pady=5)

label_replacement_date = tk.Label(frame_schedule, text="Replacement Date:")
label_replacement_date.grid(row=1, column=0, padx=5, pady=5)
entry_replacement_date = tk.Entry(frame_schedule)
entry_replacement_date.grid(row=1, column=1, padx=5, pady=5)

button_schedule = tk.Button(frame_schedule, text="Schedule Replacement", command=schedule_replacement)
button_schedule.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
