import re
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)\ ]{8,}[0-9]')

def extract_phone_number(resume_text):
  phone = re.findall(PHONE_REG, resume_text)
  if phone:
    number = ''.join(phone[0])
    if resume_text.find(number) >= 0 and len(number) <= 20:
      return number
  return None
