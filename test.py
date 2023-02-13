from pypdf import PdfWriter
import sys
merger = PdfWriter()
pdfObj = open('test.pdf', 'rb')
x = 0
for x in range(0, 30):
    merger.append(pdfObj)
    x =+1
#output = open('output.pdf', 'wb')
#merger.write(output)
merger.write(sys.stdout)
merger.close()
#output.close()