from pypdf import PdfWriter
import os

def mergePDF(path, reverseOrder, name):
    merger = PdfWriter()
    PDFs = []

    for file in os.listdir(path):
        if(file.endswith('.pdf')):
            PDFs.append(file)

    if (reverseOrder == 'Y'):
        PDFs.reverse()
    # Change current working directory
    os.chdir(path)
    for pdf in PDFs:
        merger.append(pdf)

    if (name.upper() == 'D' or name == ''):
        name = "merged-pdf.pdf"
    merger.write(f"{name}.pdf")
    merger.close()

    print("PDF Merged")


if __name__ == "__main__":
    print("pdf merger".upper().center(100))
    print(""""
NOTE:-
        1) Keep all PDFs to be merged in same folder
        2) PDFs will be merged in the order as it is kept in the folder
""")
    
    path = input("Enter Path of the Folder: ")
    reverseOrder = input("Want to reverse order (Y/N): ")
    namePDF = input("Specify Merged PDF name (Press D for Default name): ")

    mergePDF(path, reverseOrder, namePDF)