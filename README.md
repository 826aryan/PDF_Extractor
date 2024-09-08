

## PDF Processing Tool

The **PDF Processing Tool** is a Python-based application designed to extract text and images from PDF files. It utilizes `pdfplumber` to read the PDF, `pytesseract` to perform Optical Character Recognition (OCR) on images, and `OpenCV` to process images for detecting contours. The extracted data can be saved as CSV, Excel, and text files, which are automatically generated.

## Features

- Extracts text and images from a PDF file.
- Saves extracted data in CSV, Excel, and text file formats.
- Processes images using OpenCV to detect contours.
- User-friendly GUI built with Tkinter.
- Ability to browse and select PDF files and output directories.
  
## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: For building the GUI.
- **pdfplumber**: To extract text and images from PDFs.
- **pytesseract**: For OCR functionality on images.
- **PIL (Pillow)**: To handle image file operations.
- **OpenCV**: For image processing (contour detection).
- **pandas**: To save data in CSV and Excel formats.

## Prerequisites

Ensure the following dependencies are installed in your environment:

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `pdfplumber`
  - `pytesseract`
  - `Pillow`
  - `opencv-python`
  - `pandas`
  - `openpyxl` (for Excel file conversion)

To install these dependencies, run:

```bash
pip install tkinter pdfplumber pytesseract pillow opencv-python pandas openpyxl
```

Make sure you have **Tesseract-OCR** installed on your system. For instructions, visit the [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).

## How to Use

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/pdf-processing-tool.git
cd pdf-processing-tool
```

### Step 2: Run the Application

Run the following command to start the application:

```bash
python pdf_processing_tool.py
```

### Step 3: Select a PDF File and Output Directory

1. **PDF Path**: Use the "Browse" button to select the PDF file from which you want to extract text and images.
2. **Output Directory**: Use the "Browse" button to select the directory where the extracted data (CSV, Excel, and text files) will be saved.

### Step 4: Start Processing

Click the **Run Processing** button to begin the extraction process. Once completed, the application will notify you, and the following files will be saved in the output directory:

- **output_data.csv**: Contains the extracted text and paths to images.
- **output_data.xlsx**: Same as the CSV but in Excel format.
- **output_data.txt**: Contains the extracted text in a plain-text format.

### Step 5: View Extracted Files

Navigate to the output directory you selected, where you’ll find the following files:

- **output_data.csv**: A CSV file containing the text and image paths.
- **output_data.xlsx**: An Excel file with the same content as the CSV.
- **output_data.txt**: A text file with all extracted text.
- **Extracted Images**: Images extracted from the PDF will be saved with names like `page_1_image0.png`, etc.

## Code Overview

### Functions

- `extract_text_from_image(image_path)`: Uses Tesseract to extract text from an image.
- `process_pdf(pdf_path, output_dir)`: Extracts text and images from a PDF and processes each image for contour detection.
- `process_image_for_marks(image_path)`: Uses OpenCV to detect contours in the image.
- `save_to_csv(data, output_path)`: Saves extracted data to a CSV file.
- `save_to_txt(data, output_path)`: Saves extracted data to a text file.
- `convert_csv_to_excel(csv_file_path, excel_file_path)`: Converts the CSV file to an Excel file.
  
### GUI Components

- **PDF Path**: Entry field to input/select the PDF file.
- **Output Directory**: Entry field to input/select the directory where output files will be saved.
- **Run Processing Button**: Starts the PDF processing.

## Error Handling

- **Invalid PDF Path**: Displays an error message if the selected PDF file doesn't exist.
- **Invalid Output Directory**: Displays an error message if the output directory doesn't exist.
- **Exception Handling**: The program displays a message box if any unexpected error occurs during processing.

## Example Output

Below is an example of the output you'll receive after processing a PDF:
```

**CSV Output:**
| Page Number | Text                              | Images                           |
|-------------|-----------------------------------|----------------------------------|
| 1           | This is the text from page 1.     | page_1_image0.png, page_1_image1.png |
| 2           | Text from page 2 goes here.       | page_2_image0.png                |
```
## Screenshots

![PDF Processing Tool Screenshot](https://example.com/screenshot.png)  
_**Figure:** Main interface of the PDF Processing Tool_

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
