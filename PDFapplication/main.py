from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfFileMerger

def merge_pdf():  # two pdfs that are saved in director
    pdf1 = input("please enter your pdf name: (add '.pdf')")
    pdf2 = input("please enter your pdf name: (add '.pdf') ")
    pdfs = [pdf1, pdf2]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


def extractor():
    pdf_name = input("please enter your pdf name :(add '.pdf')")
    PdfFileRead = PdfFileReader(pdf_name)
    numpage = int(input("enter the page number:"))
    filename = os.path.splitext(os.path.basename(pdf_name))[0]
    PdfWriter = PdfFileWriter()
    PdfWriter.addPage(PdfFileRead.getPage(numpage - 1))
    outputFileName = '{}_newpage_{}.pdf'.format(filename, numpage)
    with open(outputFileName, 'wb') as out:
        PdfWriter.write(out)



def splitter():
    pdf_path = input("please enter pdf name to split: (add '.pdf')")
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf = PdfFileReader(pdf_path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}.page_{}.pdf'.format(file_name, page + 1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)


print("\n 1.Merge two pdfs \n 2.Extract a page from pdf\n 3.Split one Pdf into separate pages \n 4. Exit the program ")
user_choice = int(input("welcome, please choose from 1 to 4 to execute: "))
while True:

    if user_choice == 1:
        merge_pdf()
        break
    if user_choice == 2:
        extractor()
        break
    if user_choice == 3:
        splitter()
        break
    if user_choice == 4:
        print()
        print("you have been exit successfully")
        break

