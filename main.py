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

ROWS_PER_WORKSHEET = 45000

def main():
  PATH = 'test_resumes'
  files = get_files_list(PATH)
  workbook = generate_workbook()
  worksheet = generate_worksheet(workbook)

  row_number = 1 
  for index, file in enumerate(files):
    text = extract_text(file, PATH)
    source = file[1]
    names = extract_names(text)
    phone_number = extract_phone_number(text)
    emails = join_to_string(extract_emails(text))

    skills = extract_skills(text)
    skills_count = len(skills)

    if (skills_count + row_number > ROWS_PER_WORKSHEET):
      worksheet = generate_worksheet(workbook)
      row_number = 1 

    for skill in skills:
      row_number = write_to_worksheet(worksheet, row_number, source, names, phone_number, emails, skill)
    print(f"Successfully extracted data from {source}!!")

  print("Saving data to excel file!!")
  workbook.close()
  print("Data extracted successfully!!")


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

def generate_workbook():
  workbook = xlsxwriter.Workbook(str(time()) + '.xlsx')
  return workbook

def generate_worksheet(workbook):
  worksheet = workbook.add_worksheet()
  return worksheet

def write_to_worksheet(worksheet, row_number, source, name, phone_number, emails, skill):
  if (row_number == 1):
    row = str(row_number)
    worksheet.write('A' + row, "Source")
    worksheet.write('B' + row, "Name")
    worksheet.write('C' + row, "Phone Number")
    worksheet.write('D' + row, "Emails")
    worksheet.write('E' + row, "Skills")
    row_number += 1

  row = str(row_number)
  worksheet.write('A' + row, source)
  worksheet.write('B' + row, name)
  worksheet.write('C' + row, phone_number)
  worksheet.write('D' + row, emails)
  worksheet.write('E' + row, skill)
  row_number += 1

  return row_number

def join_to_string(list):
  return " ; ".join(list)

main()