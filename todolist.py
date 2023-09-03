import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()        #creating initial window
window.title("First To-Do List App by @nabidollayeva")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "Warning!", message = "You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "No data file.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    
    pickle.dump(tasks, open("tasks.dat", "wb"))
    
def mark_completed():
    marked=listbox_tasks.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_tasks.get(marked)
    #update it 
    temp_marked=temp_marked+" ✔"
    #delete it then insert it 
    listbox_tasks.delete(temp)
    listbox_tasks.insert(temp,temp_marked)

#Create GUI
frame_tasks = tkinter.Frame(window)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height = 3, width = 45, font = "Arial")
listbox_tasks.pack(side = tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)

scrollbar_tasks.config(command = listbox_tasks.yview)

entry_task = tkinter.Entry(window, width = 50)
entry_task.pack()

button_add_task = tkinter.Button(window, text = "Add task", width = 48, command = add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(window, text = "Delete selected task", width = 48, command = delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(window, text = "Load tasks", width = 48, command = load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(window, text = "Save tasks", width = 48, command = save_tasks)
button_save_tasks.pack()

mark_button = tkinter.Button(window, text = "Mark as completed", width = 48, command = mark_completed)
mark_button.pack()

window.mainloop()
