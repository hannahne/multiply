from pypdf import PdfWriter
import sys

c = int(sys.argv[2])

merger = PdfWriter()
pdfObj = open(sys.argv[1], 'rb')

for x in range(0, c):
    merger.append(pdfObj)

output = open(sys.argv[3], 'wb')
merger.write(output)
output.close()