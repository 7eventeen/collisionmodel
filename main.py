import tkinter as tk
from tkinter import ttk
import pygame
import sys
import os

pygame.init()
collisionsound = pygame.mixer.Sound('file.wav')

# GLOBAL C-VARS
tk_width = 1280   #program width
tk_height = 720  #program height
box1h = 100
box2h = 150
box1w = 100
box2w = 150


def solve_system_of_equations(v1, v2):  # return v1 & v2 after collision
    v1af = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2af = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1af, v2af


class Line:
    def __init__(self):
        self.x1 = 0
        self.y1 = tk_height - tk_height // 1.6
        self.x2 = tk_width
        self.y2 = tk_height - tk_height // 1.6
        self.line_id = canvas.create_line(self.x1, self.y1,
                                          self.x2, self.y2,
                                          fill='black', width='6')



class System:
    def __init__(self):
        self.m1 = m1 #mass of first object in system
        self.m2 = m2 #mass of second object in system
        self.v1 = v1 #velocity of first object in system before the collision
        self.v2 = v2 #velocity of second object in system before the collision

        self.box1x1, self.box1y1 = line.x2 // 5 - box1w, line.y2 - box1h
        self.box1x2, self.box1y2 = line.x2 // 5, line.y1
        self.box2x1, self.box2y1 = line.x2 - line.x2 // 5 - box2w, line.y2 - box2h
        self.box2x2, self.box2y2 = line.x2 - line.x2 // 5, line.y1

        self.box1 = canvas.create_rectangle(self.box1x1, self.box1y1, self.box1x2, self.box1y2, fill=gui.ComboBox1_m1.get())
        self.box2 = canvas.create_rectangle(self.box2x1, self.box2y1, self.box2x2, self.box2y2, fill=gui.ComboBox1_m2.get())

    def move(self):
        canvas.move(self.box1, self.v1, 0)
        canvas.move(self.box2, self.v2, 0)
        self.box1x1 += self.v1
        self.box2x1 += self.v2
        self.box1x2 += self.v1
        self.box2x2 += self.v2
        if self.box1x2 > self.box2x1:
            self.v1, self.v2 = solve_system_of_equations(self.v1, self.v2)
            gui.aLabel2_m1.config(text='mass: dm = 0, ' + str(m1) + ' kg')
            gui.aLabel3_m1.config(text='velocity after collision: ' + str(self.v1) + ' m/s')
            gui.aLabel2_m2.config(text='mass: dm = 0, ' + str(m2) + ' kg')
            gui.aLabel3_m2.config(text='velocity after collision: ' + str(self.v2) + ' m/s')
            gui.aLabel4_m1.config(text='color: ' + gui.ComboBox1_m1.get())
            gui.aLabel4_m2.config(text='color: ' + gui.ComboBox1_m2.get())
            collisionsound.play()


class GUI:
    def __init__(self):

        # BUTTON TO RUN
        self.Button1 = tk.Button(text='Start interaction',
                                  font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e',
                                 command=buttonclick)
        self.Button1.place(relx=0.1, rely=0.85, relheight=0.1, relwidth=0.3)

        self.Button2 = tk.Button(text='Restart (after interact.)',
                                 font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e',
                                 command=restart_program)
        self.Button2.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.3)

        # BEFORE INTERACTION GUI (LEFT - SIDE), m1 - 1st body, m2 - 2nd body.

        self.Label1_m1 = tk.Label(text='1st body options before interaction: (left)',
                                  font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e')
        self.Label1_m1.place(relx=0.01, rely=0.4)
        self.Label2_m1 = tk.Label(text='mass:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label2_m1.place(relx=0.01, rely=0.47)
        self.Label3_m1 = tk.Label(text='velocity before collision:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label3_m1.place(relx=0.01, rely=0.51)
        self.Label4_m1 = tk.Label(text='color:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label4_m1.place(relx=0.01, rely=0.55)

        self.Label1_m1_2 = tk.Label(text='kg', font=("Arial 32", 16), bg='#9e9e9e')
        self.Label1_m1_2.place(relx=0.118, rely=0.47)
        self.Label2_m1_2 = tk.Label(text='m/s (with minus if vector is <<<)', font=("Arial 32", 16), bg='#9e9e9e')
        self.Label2_m1_2.place(relx=0.2515, rely=0.51)


        self.Label1_m2 = tk.Label(text='2nd body options before interaction: (right)',
                                  font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e')
        self.Label1_m2.place(relx=0.01, rely=0.62)
        self.Label2_m2 = tk.Label(text='mass:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label2_m2.place(relx=0.01, rely=0.69)
        self.Label3_m2 = tk.Label(text='velocity before collision:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label3_m2.place(relx=0.01, rely=0.73)
        self.Label4_m2 = tk.Label(text='color:', font=('Arial 32', 16), bg='#9e9e9e')
        self.Label4_m2.place(relx=0.01, rely=0.77)

        self.Label1_m2_2 = tk.Label(text='kg', font=("Arial 32", 16), bg='#9e9e9e')
        self.Label1_m2_2.place(relx=0.118, rely=0.69)
        self.Label2_m2_2 = tk.Label(text='m/s (with minus if vector is <<<)', font=("Arial 32", 16), bg='#9e9e9e')
        self.Label2_m2_2.place(relx=0.2515, rely=0.73)


        self.ComboBox1_m1 = ttk.Combobox(values=["white", "black", "red", "green", "blue", "cyan", "yellow"],
                                         font=("Arial 32", 16))
        self.ComboBox1_m1.place(relx=0.06, rely=0.55)


        self.ComboBox1_m2 = ttk.Combobox(values=["white", "black", "red", "green", "blue", "cyan", "yellow"],
                                         font=("Arial 32", 16))
        self.ComboBox1_m2.place(relx=0.06, rely=0.77)


        self.Entry1_m1 = tk.Entry(font=('Arial 32', 16), bg='#9e9e9e')
        self.Entry1_m1.place(relx=0.06, rely=0.47, width=75)
        self.Entry2_m1 = tk.Entry(font=('Arial 32', 16), bg='#9e9e9e')
        self.Entry2_m1.place(relx=0.194, rely=0.51, width=75)


        self.Entry1_m2 = tk.Entry(font=('Arial 32', 16), bg='#9e9e9e')
        self.Entry1_m2.place(relx=0.06, rely=0.69, width=75)
        self.Entry2_m2 = tk.Entry(font=('Arial 32', 16), bg='#9e9e9e')
        self.Entry2_m2.place(relx=0.194, rely=0.73, width=75)

        #AFTER INTERACTION GUI (RIGHT - SIDE), m1 - 1st body, m2 - 2nd body.

        self.aLabel1_m1 = tk.Label(text='1st body options after interaction:',
                                  font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e')
        self.aLabel1_m1.place(relx=0.6, rely=0.4)
        self.aLabel2_m1 = tk.Label(text='mass: ' + 'x' + ' kg', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel2_m1.place(relx=0.6, rely=0.47)
        self.aLabel3_m1 = tk.Label(text='velocity after collision: ' + 'x' + ' m/s', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel3_m1.place(relx=0.6, rely=0.51)
        self.aLabel4_m1 = tk.Label(text='color: ' + 'x', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel4_m1.place(relx=0.6, rely=0.55)


        self.aLabel1_m2 = tk.Label(text='2nd body options after interaction:',
                                  font=("Comic Sans MS", 22, "bold"), bg='#9e9e9e')
        self.aLabel1_m2.place(relx=0.6, rely=0.62)
        self.aLabel2_m2 = tk.Label(text='mass: ' + 'x' + ' kg', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel2_m2.place(relx=0.6, rely=0.69)
        self.aLabel3_m2 = tk.Label(text='velocity after collision: ' + 'x' + ' m/s', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel3_m2.place(relx=0.6, rely=0.73)
        self.aLabel4_m2 = tk.Label(text='color: ' + 'x', font=('Arial 32', 16), bg='#9e9e9e')
        self.aLabel4_m2.place(relx=0.6, rely=0.77)


def restart_program():
    """Restarts the current program"""
    python = sys.executable
    os.execl(python, python, *sys.argv)


def tick():
    system.move()
    root.after(70, tick)


def buttonclick():
    global system, m1, m2, v1, v2
    m1 = float(gui.Entry1_m1.get())  # mass of first object in system
    m2 = float(gui.Entry1_m2.get())  # mass of second object in system
    v1 = float(gui.Entry2_m1.get())  # velocity of second object in system before collision
    v2 = float(gui.Entry2_m2.get())
    canvas.delete('all')
    system = System()
    tick()


def main():
    global root, canvas, line, gui
    root = tk.Tk()
    root.configure(bg='#9e9e9e')
    root.geometry(str(tk_width) + "x" + str(tk_height))
    canvas = tk.Canvas(root, bg='#9e9e9e')
    canvas.place(width=tk_width, height=tk_height - tk_height // 1.6)
    #canvas = tk.Canvas(root, width=tk_width, height=(tk_height - tk_height // 1.6), bg='#9e9e9e')
    #canvas.pack()
    gui = GUI()
    line = Line()
    root.mainloop()


if __name__ == '__main__':
    main()


