import xmlrpc.client as cl
import tkinter as tk

class GUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("700x400")
        self.root.title("ClientProgram")

        self.toplable=tk.Label(self.root, text="Client Interface", font=("Arial",18))
        self.toplable.pack(padx=10,pady=10, side="top")

        self.IPframe=tk.Frame(self.root)
        self.IPframe.columnconfigure(0,weight=1)

        self.IPlable=tk.Label(self.IPframe, text="Enter Server IP : ",font=("Arial",12))
        self.IPlable.grid(row=0,column=0, padx=10)

        self.IPEntry=tk.Entry(self.IPframe,font=("Arial",11))
        self.IPEntry.grid(row=0,column=1, padx=10)

        self.IPframe.pack(padx=10,pady=10,anchor="nw")

        self.Msglable=tk.Label(self.root, text="Message : ",font=("Arial",12))
        self.Msglable.pack(padx=20,pady=10,anchor="nw")

        self.textbox=tk.Text(self.root,height=10,font=("Arial",11))
        self.textbox.pack(padx=10,pady=10)

        self.display=tk.Button(self.root,text="Show Message",font=("Arial",11),command=self.showMsg,bg="#F6FFA4")
        self.display.pack(padx=10,pady=10)

        self.root.mainloop()

    def showMsg(self):
        IP = self.IPEntry.get()
        server = cl.ServerProxy(str("http://"+IP+":8000/"))
        result = server.show()
        self.textbox.insert("1.0", result + "\n")


if __name__=="__main__":
    GUI()