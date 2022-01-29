from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
import numpy as np
from fastapi import Response
from typing import Optional
import json
from urllib.parse import unquote
import base64

app = FastAPI()
def function(url):
	url = unquote(url)
	#url = "https://www.amazon.com.br/Mouse-Desk-Couro-Ecologico-90x40cm/dp/B08NFBXSJK/ref=asc_df_B08NFBXSJK/?tag=googleshopp00-20&linkCode=df0&hvadid=379725868941&hvpos=&hvnetw=g&hvrand=15667433486320440314&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001538&hvtargid=pla-1156429427409&psc=1"
	print(os.listdir())
	arq = open('testes/dominio.txt','w')
	arq.write(url)
	arq.close()
	os.system('scrapy runspider testes/amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_review.py -o testes/reviews.csv')
	dataset = pd.read_csv('testes/reviews.csv',names=['star','comment'])
	#dataset['comment'] = dataset['comment'].apply(lambda x: x.replace('\n',''))#.iloc[-1]#.values
	port= []
	for x in dataset.values:
	    if "estrelas" in x[0]:
	        port.append({'star':x[0].split('de')[0].replace('','').replace(',','.'),'comment':x[1]})
	port = pd.DataFrame(port)
	arq = open('testes/reviews.csv','w')
	arq.write('')
	arq.close()
	return port.to_dict(orient='records')
import base64
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

@app.get("/get_coments/{url_produto}")
def read_item(url_produto: str):
	#base64_message = 'UHl0aG9uIGlzIGZ1bg=='
	print('------',url_produto)
	base64_bytes = unquote(url_produto).encode('ascii')
	print('------',base64_bytes)
	message_bytes = base64.b64decode(base64_bytes)
	print('------',message_bytes)
	message = message_bytes.decode('ascii')
	print(message)
	print(function(message))
	return Response(status_code=200, content=json.dumps(function(message)), media_type='application/json')
