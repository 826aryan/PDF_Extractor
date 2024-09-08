import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import pytesseract
import pdfplumber
from PIL import Image
import cv2
import pandas as pd

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to process a PDF file and extract text and images
def process_pdf(pdf_path, output_dir):
    pdf = pdfplumber.open(pdf_path)
    page_data = []
    for page_num, page in enumerate(pdf.pages):
        images = page.images
        image_paths = []
        for i, img in enumerate(images):
            bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
            img_obj = page.within_bbox(bbox).to_image()
            image_path = os.path.join(output_dir, f"page_{page_num + 1}_image{i}.png")
            img_obj.save(image_path)
            image_paths.append(image_path)
            process_image_for_marks(image_path)
        text = page.extract_text()
        page_data.append({
            'page_number': page_num + 1,
            'text': text,
            'images': image_paths
        })
    pdf.close()
    return page_data

def process_image_for_marks(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

def save_to_csv(data, output_path):
    flattened_data = []
    for page in data:
        flattened_data.append({
            'Page Number': page['page_number'],
            'Text': page['text'],
            'Images': ', '.join(page['images'])
        })
    df = pd.DataFrame(flattened_data)
    df.to_csv(output_path, index=False)

def convert_csv_to_excel(csv_file_path, excel_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_excel(excel_file_path, index=False, engine='openpyxl')
    messagebox.showinfo("Success", f"Converted {csv_file_path} to {excel_file_path}")

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_pdf_path.delete(0, tk.END)
    entry_pdf_path.insert(0, file_path)

def browse_output_dir():
    dir_path = filedialog.askdirectory()
    entry_output_dir.delete(0, tk.END)
    entry_output_dir.insert(0, dir_path)

def run_processing():
    pdf_path = entry_pdf_path.get()
    output_dir = entry_output_dir.get()
    
    if not pdf_path or not output_dir:
        messagebox.showerror("Error", "Please specify both PDF file and output directory.")
        return
    
    if not os.path.isfile(pdf_path):
        messagebox.showerror("Error", "PDF file does not exist.")
        return
    
    if not os.path.isdir(output_dir):
        messagebox.showerror("Error", "Output directory does not exist.")
        return
    
    try:
        page_data = process_pdf(pdf_path, output_dir)
        
        csv_file_path = os.path.join(output_dir, "output_data.csv")
        excel_file_path = os.path.join(output_dir, "output_data.xlsx")
        
        save_to_csv(page_data, csv_file_path)
        convert_csv_to_excel(csv_file_path, excel_file_path)
        
        messagebox.showinfo("Success", f"Processing complete. Files saved to {output_dir}.")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("PDF Processing Tool")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_pdf_path = ttk.Label(frame, text="PDF Path:")
label_pdf_path.grid(row=0, column=0, sticky=tk.W)

entry_pdf_path = ttk.Entry(frame, width=50)
entry_pdf_path.grid(row=0, column=1, padx=5)

button_browse_pdf = ttk.Button(frame, text="Browse", command=browse_pdf)
button_browse_pdf.grid(row=0, column=2, padx=5)

label_output_dir = ttk.Label(frame, text="Output Directory:")
label_output_dir.grid(row=1, column=0, sticky=tk.W)

entry_output_dir = ttk.Entry(frame, width=50)
entry_output_dir.grid(row=1, column=1, padx=5)

button_browse_output_dir = ttk.Button(frame, text="Browse", command=browse_output_dir)
button_browse_output_dir.grid(row=1, column=2, padx=5)

button_run = ttk.Button(frame, text="Run Processing", command=run_processing)
button_run.grid(row=2, column=0, columnspan=3, pady=10)

app.mainloop()