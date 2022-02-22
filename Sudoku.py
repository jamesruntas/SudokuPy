import tkinter as tk
 
 
def press(cell):
    #increment cell number
    if cell['text']=='':
        cell['text'] = 1
    elif cell['text']==9:
        cell['text']=''
    else:
        cell['text'] = (cell['text'] % 9) + 1
 
 
def Solve():
   print("solving")
 
def makeBoard():

    gui = tk.Tk()
    gui.configure(background="light green")
    gui.title("Sudoku Solver")
    gui.geometry("450x450")


  

    test_cmd = gui.register(Solve())
    num = []
    for i in range(81):
        e = tk.StringVar()
        num.append(e)

    entrys = []
    x = 0
    L = 'lemon chiffon'
    D = 'DodgerBlue2'
    colors = [L, L, L, D, D, D, L, L, L,
         L, L, L, D, D, D, L, L, L,
         L, L, L, D, D, D, L, L, L,
         D, D, D, L, L, L, D, D, D,
         D, D, D, L, L, L, D, D, D,
         D, D, D, L, L, L, D, D, D,
         L, L, L, D, D, D, L, L, L,
         L, L, L, D, D, D, L, L, L,
         L, L, L, D, D, D, L, L, L]
    for i in range(9):
        
        for j in range(9):
            e = tk.Button(gui, text='', bg=colors[x],height=2,width=4)
            e['command'] = lambda widget=e: press(widget)
            e.grid(row=i, column=j, padx=4, pady=4)
            entrys.append(e)
            x += 1
            

    gui.mainloop()

def clear(cells):
    for cell in cells:
        print("clearing")
 
    
 
if __name__ == "__main__":
    makeBoard()