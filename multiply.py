from pypdf import PdfWriter
import sys

if len(sys.argv) < 4:
    print("usage: multiply <inputfile> <number_of_copies> <outputfile>")
    exit(1)

c = int(sys.argv[2])

merger = PdfWriter()
pdfObj = open(sys.argv[1], 'rb')

for x in range(0, c):
    merger.append(pdfObj)

pdfObj.close()

output = sys.argv[3]
output_file = open(output, "wb")
merger.write(output)
output_file.close()
