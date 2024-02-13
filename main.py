from os import listdir
from os.path import isfile, join

import xlsxwriter
from time import time

from text.docx import extract_text_from_docx
from text.pdf import extract_text_from_pdf

from resume.extract_names import extract_names
from resume.extract_phone_number import extract_phone_number
from resume.extract_emails import extract_emails
from resume.extract_skills import extract_skills
from resume.extract_education import extract_education

def main():
  PATH = 'test_resumes'
  files = get_files_list(PATH)
  [output, output_sheet] = generate_output_file()

  for index, file in enumerate(files):
    text = extract_text(file, PATH)
    source = file[1]
    names = extract_names(text)
    phone_number = extract_phone_number(text)
    emails = join_to_string(extract_emails(text))
    skills = join_to_string(extract_skills(text))
    education = join_to_string(extract_education(text))

    write_to_output_sheet(output_sheet, index, source, names, phone_number, emails, skills, education)

  output.close()


def get_files_list(path):
  files = [f for f in listdir(path) if isfile(join(path, f))]
  files = list(map(lambda x: [x.split('.')[-1], x], files))
  files = [f for f in files if f[0] in ['pdf', 'docx']]
  return files

def extract_text(file_data, path):
  match file_data[0]:
    case 'docx':
      text = extract_text_from_docx(path + '/' + file_data[1])
    case 'pdf':
      text = extract_text_from_pdf(path + '/' + file_data[1])
  return text

def generate_output_file():
  workbook = xlsxwriter.Workbook(str(time()) + '.xlsx')
  worksheet = workbook.add_worksheet()
  return [workbook, worksheet]

def write_to_output_sheet(output_sheet, index, source, names, phone_number, emails, skills, education):
  if (index == 0):
    row = str(index + 1)
    output_sheet.write('A' + row, "source")
    output_sheet.write('B' + row, "names")
    output_sheet.write('C' + row, "phone_number")
    output_sheet.write('D' + row, "emails")
    output_sheet.write('E' + row, "skills")
    output_sheet.write('F' + row, "education")

  row = str(index + 2)
  output_sheet.write('A' + row, source)
  output_sheet.write('B' + row, names)
  output_sheet.write('C' + row, phone_number)
  output_sheet.write('D' + row, emails)
  output_sheet.write('E' + row, skills)
  output_sheet.write('F' + row, education)

def join_to_string(list):
  return " ; ".join(list)

main()