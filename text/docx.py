import docx2txt

def extract_text_from_docx(docx_path):
  txt = docx2txt.process(docx_path)
  if txt:
    return txt.replace('\t', ' ')
  return None
