Steps Taken :
	1:-- Downloaded and read the excel file using pandas in the format as required.
	2:-- Sent request to the urls using request method and extracted required fields using xpath constructor..
	3:-- Uploaded the data extracted in required json dict form in file amazon_data.json..
	4:-- Uploaded all the files by creating gitlab link and uploaded the gitlab link in the docs..
	
	
Bonus Task Steps :
	1:-- Read the image shown in the captcha using python library pytesseract and then passed the captcha in the required url to get reaponse of the url.
	Request url format :-- f'https://www.amazon.com/errors/validateCaptcha?amzn=vac3Ri%2BlTsAct2GvJyz9JQ%3D%3D&amzn-r=%2F&field-keywords={text}' (where text is the captcha text extracted). 