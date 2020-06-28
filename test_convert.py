import pytest
import utils 
import convertapi
import os

def test_docx_to_pdf():
    imp = "docx"
    exp = "pdf"
    convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
    conv = convertapi.UploadIO(open('./test_file/DOCX_TO_PDF.docx', 'rb'))
    p = utils.convert(imp, exp, conv).read()
    exp_pdf = open('./convertedFile.pdf', 'rb').read()
    assert p == exp_pdf

def test_pdf_to_docx():
    imp = "pdf"
    exp = "docx"
    convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
    conv = convertapi.UploadIO(open('./test_file/PDF_TO_DOCX.pdf', 'rb'))
    p = utils.convert(imp, exp, conv).read()
    exp_docx = open('./convertedFile.docx', 'rb').read()
    assert p == exp_docx

def test_pdf_to_png():
    imp = "pdf"
    exp = "png"
    convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
    conv = convertapi.UploadIO(open('./test_file/PDF_TO_PNG.pdf', 'rb'))
    p = utils.convert(imp, exp, conv).read()

    exp_png = open('./test_file/PDF_TO_PNG.png', 'rb').read()
    assert p == exp_png

def test_docx_to_jpeg():
    imp = "docx"
    exp = "jpg"
    convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
    conv = convertapi.UploadIO(open('./test_file/DOCX_TO_JPG.docx', 'rb'))
                                                 # Сохранение в текущую директорию
    p = utils.convert(imp, exp, conv).read()

    exp_jpg = open('./test_file/DOCX_TO_JPG.jpg', 'rb').read()
    assert p == exp_jpg

pytest.main()