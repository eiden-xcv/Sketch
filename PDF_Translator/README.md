# PDF_Translator

## 영문 pdf파일을 한글 txt파일로 전환해주는 프로그램
- PDF 읽기 : pdfminer 활용
- 언어 번역 : Papago API와 googletrans 라이브러리(Google Translate API)를 활용

## 보완할 점
- pdf -> txt 전환 시, 페이지 간 긴 공백이 생김
  - 문장이 끊기는 문제가 생길 수 있으니 공백 제거해야함
- papago_translate() 사용시, Papago API 글자수 제한이 있기에 5000자 이하만 번역 및 전환 가능
  - 5000자씩 끊어서 번역해야함( + Papago API는 하루 10000단어 제한 있음 )
- download_pdf() 생각해보기
