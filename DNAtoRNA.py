import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("DNA to RNA Converter")

# Create entry box for user DNA input
dna_entry_label = tk.Label(window, text="Enter DNA Strand (A, C, G, T only):")
dna_entry_label.pack()
dna_entry = tk.Entry(window, width=50)
dna_entry.pack()

# Create the DNA canvas
dna_canvas = tk.Canvas(window, width=500, height=50)
dna_canvas.pack()

# Create the RNA canvas
rna_canvas = tk.Canvas(window, width=500, height=100)
rna_canvas.pack()

# Create the RNA label
rna_label = tk.Label(window, text="RNA: ")
rna_label.pack()

# Color map for nucleotides
color_map = {
    "A": "#FFC107",  # Orange
    "C": "#2196F3",  # Blue
    "G": "#4CAF50",  # Green
    "T": "#009688",  # Teal
    "U": "#E91E63"   # Pink
}

dna_rectangles = []
dna_text = []
rna_rectangles = []
rna_text = []
dna_strand = ""
rna_strand = ""

def update_dna_colors():
    dna_canvas.delete("all")
    global dna_rectangles, dna_text
    dna_rectangles, dna_text = [], []
    for i, base in enumerate(dna_strand):
        x1, y1, x2, y2 = 5 + 50 * i, 5, 45 + 50 * i, 40
        rect = dna_canvas.create_rectangle(x1, y1, x2, y2, fill=color_map[base])
        text = dna_canvas.create_text(x1 + 20, y1 + 20, text=base)
        dna_rectangles.append(rect)
        dna_text.append(text)

def update_rna_colors():
    rna_canvas.delete("all")
    global rna_rectangles, rna_text
    rna_rectangles, rna_text = [], []
    for i, base in enumerate(rna_strand):
        x1, y1, x2, y2 = 5 + 50 * i, 5, 45 + 50 * i, 55
        rect = rna_canvas.create_rectangle(x1, y1, x2, y2, fill=color_map[base])
        text = rna_canvas.create_text(x1 + 20, y1 + 25, text=base)
        rna_rectangles.append(rect)
        rna_text.append(text)

def convert_to_rna():
    global dna_strand, rna_strand
    dna_input = dna_entry.get().upper()
    
    # Validate input
    if not all(base in "ACGT" for base in dna_input):
        messagebox.showerror("Invalid Input", "Please enter only A, C, G, or T.")
        return
    
    dna_strand = dna_input
    rna_strand = dna_strand.replace("T", "U")
    
    update_dna_colors()
    update_rna_colors()
    rna_label.config(text=f"RNA: {rna_strand}")

# Create the convert button
convert_button = tk.Button(window, text="Convert to RNA", command=convert_to_rna)
convert_button.pack()

# Start the main loop
window.mainloop()
