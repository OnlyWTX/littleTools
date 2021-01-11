import sys
import os
# from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator


def execute(input, output):
    try:
        fileList = os.listdir(input)
        # 跳出json数据
        for file in fileList:
            if ('.' in file) and (file.split('.')[1] == 'pdf'):
                pdf_file = input + '/' + file
                fileName = file.split('.')[0]
                break
        with open(pdf_file, 'rb') as f:
            parser = PDFParser(f)
            doc = PDFDocument(parser) 
            parser.set_document(doc)
            rsrcmgr = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if isinstance(x, LTTextBoxHorizontal):
                        with open(output + '/' + fileName + '.doc','a',encoding='utf-8') as f1:
                            results = x.get_text()
                            f1.write(results+'\n')
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')