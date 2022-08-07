import requests, json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from googletrans import Translator
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

eng_file_name='eng_file.txt'
kor_file_name='kor_file.txt'

# Google scholar에서 검색 후 다운로드 하는 함수
# pdf만 골라서 다운로드 받기가 흠...... 
def download_pdf():
  # title=input('찾을 논문을 입력하시오 : ')

  # driver = webdriver.Chrome()
  # driver.get('https://scholar.google.com/')
  # time.sleep(3)

  # driver.find_element(By.CSS_SELECTOR,'#gs_hdr_tsi').send_keys(title)
  # driver.find_element(By.CSS_SELECTOR, '#gs_hdr_tsb').click()
  pass


def pdf_to_txt(pdf_file):
  ef=open(eng_file_name,'w',encoding='utf-8')

  for page_layout in extract_pages(pdf_file):
    for element in page_layout:
      if isinstance(element, LTTextContainer):
        ef.write(element.get_text())
  
  ef.close()  


def papago_translate():
  """
  This function is translating english to korean.
  But, Only works on document up to 5000 characters.
  """
  with open(eng_file_name,'r',encoding='utf-8') as file:
    eng_text=file.read()
    
  CLIENT_ID, CLIENT_SECRET = "yourID", "yourSECRET"    
  
  url_papago="https://openapi.naver.com/v1/papago/n2mt"
  headers= { 
      'Content-Type' : 'application/json', 
      'X-Naver-Client-Id':CLIENT_ID,
      'x-Naver-Client-Secret':CLIENT_SECRET,
  }

  params={ 'source' : 'en', 'target' : 'ko', 'text' : eng_text }

  response=requests.post(url_papago, json.dumps(params), headers=headers)
  
  try :
    kor_text=response.json()['message']['result']['translatedText']
    
    kf=open(kor_file_name,'w',encoding='utf-8')
    kf.write(kor_text)
    kf.close()
    
    print('Success')
  except Exception as e:
    print(f'Failed : {response}')


def googletrans_translate():
  with open(eng_file_name,'r',encoding='utf-8') as file:
    eng_text=file.read()
  
  translator=Translator()
  kor_text=translator.translate(text=eng_text, src='en', dest='ko')

  try:
    kf=open(kor_file_name,'w',encoding='utf-8')
    kf.write(kor_text.text)
    kf.close()
    
    print('Success')
  except Exception as e:
    print(f'Failed : {e}')
  
  
def main():
  target_pdf=input('디렉토리 내 번역할 pdf 문서명을 입력하시오 : ')
  target_pdf+='.pdf'
  pdf_to_txt(target_pdf)
  # papago_translate()
  googletrans_translate()
  
main()