from pypdf import PdfWriter
import sys
c = int(sys.argv[2])
merger = PdfWriter()
pdfObj = open(sys.argv[1], 'rb')
x = 0
for x in range(0, c):
    merger.append(pdfObj)
    x =+1
output = open(sys.argv[3], 'wb')
merger.write(output)
output.close()