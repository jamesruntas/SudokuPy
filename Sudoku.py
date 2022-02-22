import tkinter as tk

from matplotlib.pyplot import grid
 
 
def press(cell,entrys):
    #increment cell number
    if cell['text']=='':
        cell['text'] = 1
    elif cell['text']==9:
        cell['text']=''
    else:
        cell['text'] = (cell['text'] % 9) + 1
  
def makeBoard():

    gui = tk.Tk()
    gui.configure(background="light green")
    gui.title("Sudoku Solver")
    gui.geometry("450x500")

    num = []
    for i in range(81):
        e = tk.StringVar()
        num.append(e)

    x = 0
    entrys =[]
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
            e['command'] = lambda widget=e: press(widget,entrys)
            e.grid(row=i, column=j, padx=4, pady=4)
            entrys.append(e)
            x += 1
    
    solveButton = tk.Button(gui, text='Solve', bg='yellow',height=2,width=4)
    solveButton['command'] = lambda widget=solveButton: Solve(entrys)
    solveButton.grid(row=11, column=4, padx=4, pady=4)

    clearButton = tk.Button(gui, text='Clear', bg='light blue',height=2,width=4)
    clearButton['command'] = lambda widget=clearButton: clear(entrys)
    clearButton.grid(row=11, column=5, padx=4, pady=4)

    gui.mainloop()

def clear(entrys):
    for cell in entrys:
         cell['text'] = ''
 
def Solve(board):
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x] = n
                        Solve(grid)
                        grid[y][x] = 0
                return 
    print(grid)

def possible(y,x,n):
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range (0,9):
        if grid[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

 
if __name__ == "__main__":
    makeBoard()