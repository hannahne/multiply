from pypdf import PdfWriter
import sys

c = int(sys.argv[2])

merger = PdfWriter()
pdfObj = open(sys.argv[1], 'rb')

for x in range(0, c):
    merger.append(pdfObj)

output = sys.argv[3]+'.pdf'
open(output, "wb")
merger.write(output)