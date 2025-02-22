import PyPDF2
import json

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page in range(num_pages):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()
    return text

def extract_tables_from_pdf(text):
    lines = text.split('\n')
    tables = []
    table = []
    for line in lines:
        if line.strip() == "":
            if table:
                tables.append(table)
                table = []
        else:
            table.append(line.strip())
    if table:
        tables.append(table)
    return tables

def save_to_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    pdf_file_path = input("Enter the path of PDF file: ").strip()
    text = extract_text_from_pdf(pdf_file_path)
    tables = extract_tables_from_pdf(text)
    data = {
        "headers": text.split('\n\n'),
        "List_items": tables
    }
    json_file_path = pdf_file_path.split('.')[0] + '.json'
    save_to_json(json_file_path, data)
    print("Data saved to", json_file_path)

if __name__ == "__main__":
    main()