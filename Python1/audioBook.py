#python text to speech
import pyttsx3
import PyPDF2

book = open('oop.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)
a=pyttsx3.init()
page= pdfReader.getPage(7)
text=page.extractText()
a.say(text)
a.runAndWait()

