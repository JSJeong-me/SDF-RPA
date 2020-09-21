
import camelot
import sys
tables=camelot.read_pdf(sys.argv[1])
tables[0].to_excel(sys.argv[2])