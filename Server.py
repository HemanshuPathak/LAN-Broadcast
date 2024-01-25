import xmlrpc.server as sc
import tkinter as tk
import threading
import socket

server=None
server_thread = None
server_running = False

class GUI:
    def __init__(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.ip_address=ip_address

        self.root=tk.Tk()
        self.root.geometry("700x360")
        self.root.title("ServerProgram")

        self.toplable=tk.Label(self.root, text="Generate Server", font=("Arial",18))
        self.toplable.pack(padx=10,pady=10, side="top")
        
        self.ip=tk.Label(self.root, text="IP Address :"+ self.ip_address, font=("Arial",12))
        self.ip.pack(side="top",padx=10, anchor="n")

        self.text=tk.Label(self.root, text="Enter Text :", font=("Arial",12))
        self.text.pack(side="top",padx=10, anchor="nw")
        
        self.textbox=tk.Text(self.root,height=10,font=("Arial",11))
        self.textbox.pack(padx=0,pady=10)
        
        self.buttonframe=tk.Frame(self.root)
        self.buttonframe.columnconfigure(0,weight=1)
        
        self.btn1=tk.Button(self.buttonframe,text="Start Server",font=("Arial",12),command=self.start,bg="#9ADE7B")
        self.btn1.grid(row=0,column=0, padx=70)
        
        self.btn2=tk.Button(self.buttonframe,text="Stop Server",font=("Arial",12),command=self.stop,bg="#FF6868")
        self.btn2.grid(row=0,column=1,padx=70)

        self.btn3=tk.Button(self.buttonframe,text="Exit",font=("Arial",12),command=self.Exit,bg="black",fg="white")
        self.btn3.grid(row=0,column=2,padx=70)
        
        self.buttonframe.pack(pady=20)
        self.root.mainloop()
    
    def show(self):
        return self.textbox.get('1.0',tk.END)
    
    def start(self):
        global server, server_running, server_thread
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        server = sc.SimpleXMLRPCServer((str(ip_address), 8000))
        server.register_function(self.show,"show")
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        server_running = True
    
    def stop(self):
        global server, server_running, server_thread
        server.shutdown()
        server_thread.join()
        server_running = False

    def Exit(self):
        global server_running
        if server_running == True:
            self.stop()
        self.root.quit()

if __name__=="__main__":
    GUI()
