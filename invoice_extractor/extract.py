from io import StringIO

import pdfplumber
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI




def extract_data(html):
    llm = ChatOpenAI(temperature=0, model_name='gpt-4')

    prompt = PromptTemplate.from_template("""Given the following invoice text is extracted from pdf file. Extract these data
    from this text
    - sender: the company sending the invoice, creditor
    - sender address
    - Recipient: the company that needs to pay the invoice, debtor
    - Recipient address 
    - invoice date in ISO 8601 format
    - invoice number
    - total amount
    - total vat
    - total amount including vat 
    
    Output in json format, and don't add any explanations. I only want the json output.
    Don't make up any data. If you can't fill some of the fields, you can put null values. 

    --- output format ---
    {{
      "sender": "ABC Corporation",
      "sender_address": "123 Main Street, Cityville, USA",
      "recipient": "XYZ Enterprises",
      "recipient_address": "456 Market Avenue, Townville, USA",
      "invoice_date": "2023-07-21",
      "invoice_number": "INV-20230721-001",
      "total_amount": 1000.00,
      "total_vat": 200.00,
      "total_amount_including_vat": 1200.00
    }}
   
    --- invoice ----
    {invoice}""")
    prompt.format(invoice="colorful socks")

    chain = LLMChain(llm=llm, prompt=prompt)
    data = chain.run(html)
    return data

def extract_pdf_to_html(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as fin:
        extract_text_to_fp(fin, output_string, maxpages=1, laparams=LAParams(),
                           output_type='html', codec=None)
    return output_string.getvalue()

def extract_text_from_html(html_content):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    all_text = soup.get_text()
    print(all_text)
    return all_text

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ''
        for page in pdf.pages:
            all_text += page.extract_text()

    return all_text

def extract_invoice_data_from_pdf(pdf_file):
    fns = [extract_text_from_pdf, extract_data]
    t = pdf_file
    for fn in fns:
        t = fn(t)
    return t

if __name__ == "__main__":
    pdf_file_path = './test_docs/Zakelijke-factuur-NL98INGB0007898615-20230401-20230430.pdf'
    # html_output = extract_pdf_to_html(pdf_file_path)
    # text = extract_text_from_html(html_output)
    # text = extract_text_from_pdf(pdf_file_path)
    # output = extract_data(text)
    output = extract_invoice_data_from_pdf(pdf_file_path)
    print(output)
