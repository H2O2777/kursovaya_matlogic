#Самокрутов АС-22-04 Диаграммы Венна
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import tkinter as tk
from tkinter import ttk

def submit():
    formula = entry.get()
    plotdiagram(formula)
    
def plotdiagram(formula, filename='venndiagram.png'):
    plt.figure(figsize=(8, 8))
    v = venn3(alpha=0.7, subsets=(1, 1, 1, 1, 1, 1, 1), set_colors=['white']*3, subset_label_formatter=lambda x: '')
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed', linewidth=2)
    for region in listregions(formula):
        if region == '000':
            plt.gca().set_facecolor('grey')
        else:
            v.get_patch_by_id(region).set_color('grey')
    plt.title('Venn Diagram', fontsize=16)
    plt.savefig(filename)
    plt.show()

def listregions(formula):
    from itertools import product
    ABC = ['A', 'B', 'C']
    values = product([False, True], repeat=3)
    for x in values:
        assignments = dict(zip(ABC, x))
        if eval(formula, {}, assignments):
            yield ''.join(str(int(assignments[var])) for var in ABC)

root = tk.Tk()
root.title('Venn Diagram')
root.geometry('300x100')

label = ttk.Label(root, text="Enter the formula:")
label.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Submit", command=submit)
button.pack()

root.mainloop()