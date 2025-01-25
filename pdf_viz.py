import os
import camelot 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

file_name = 'corretora_jornada_de_dados (1)'
base_path = r"D:\Data Engineer Journey\ETL-ConverterPDF\Files\jornada"
file_path = os.path.join(base_path, f"{file_name}.pdf")


tables = camelot.read_pdf(
  file_path,
  pages = '1-end',
  flavor = 'stream',
  table_areas = ['65, 558, 500, 298'],
  columns=["65,107,156,212,288,336,383,450"],
  strip_text = " .\n"
)

print(tables[0].parsing_report)

#camelot.plot(tables[0], kind="contour")
#plt.show()

print(tables[0].df)
print("Pause")

