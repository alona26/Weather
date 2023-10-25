import tkinter as tk
from weatherApp import get_data



class HomePage():
#creating window

    def __init__(self,master):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.namePlace = tk.StringVar() 
        self.label = tk.Label(master,text="Place name")
        self.entry = tk.Entry(master,textvariable= self.namePlace)
        self.button = tk.Button(master,text="Submit", command = lambda: self.display_data(self.dataDisplay,self.namePlace))
        self.dataDisplay = tk.Label(master,text="The result appear here")
        self.label.pack()

        self.entry.pack()
        self.button.pack()
        self.dataDisplay.pack(pady=20)

    def display_data(self, dataDisplay,namePlace):

        data = get_data(namePlace) # Calling backend function to get data
        print(data)
        dataDisplay.config(text=data['cod'])  # Update the label with the fetched data
    
def main():
    root=tk.Tk()
    app = HomePage(root)
    root.mainloop()
        
if __name__ == "__main__":
    main()