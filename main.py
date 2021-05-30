import pywhatkit

## Menggunakan variable untuk menulis string jadi tulisan tangan

# text = "Hello temen-temen\nDi post kali ini\n"
# text = text + "Gw akan mencoba untuk menulis tangan dengan python"
# pywhatkit.text_to_handwriting(text,rgb=[0,0,0])


## Menggunakan file txt untuk diubah total jadi tulisan tangan

def txtToHandwriting():
  # baca txt
  file_1 = open('text.txt', 'r')
  count = 0
  final_text = []

  # masukin isi filenya ke dalam list final_text
  while True:
    count += 1
    # kita baca filenya per baris
    line = file_1.readlines()

    if not line:
      break

    final_text.append(line)
  file_1.close()

  # gabung semua str di dalem list dan catet karena hanya bisa terima text, bukan list
  temp = ''
  for text in final_text[0]:
    temp += text
    print(text)

  pywhatkit.text_to_handwriting(temp,rgb=[0,0,0])
  print('Conversion Completed!')


# panggil fungsinya
txtToHandwriting()