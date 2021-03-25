# -*- coding: utf-8 -*-
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as elemTree
import pymysql as my
import cx_Oracle
con=cx_Oracle.connect("oneteam/enffl@localhost:1521/xe")
cur = con.cursor()
sql = "insert into companycode values (s_companycode.nextval,'{}','{}')"
API_key = ""
url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=" + API_key
resp = urlopen(url)
# print(resp)

with ZipFile(BytesIO(resp.read())) as zf:
    file_list = zf.namelist()
    while len(file_list) > 0:
        file_name = file_list.pop()
        corpCode = zf.open(file_name).read().decode()

tree = elemTree.fromstring(corpCode)

XML_stocklist = tree.findall("list")

corp_code = [x.findtext("corp_code") for x in XML_stocklist]
corp_name = [x.findtext("corp_name") for x in XML_stocklist]
stock_code = [x.findtext("stock_code") for x in XML_stocklist]
modify_date = [x.findtext("modify_date") for x in XML_stocklist]

stocklist = {}

for i in range(len(corp_code)):
    stocklist[corp_code[i]] = (corp_name[i], corp_code[i])
for i in corp_code:
    # print(stocklist[i][0])
    # print(stocklist[i][1])
    company=stocklist[i][0]
    code=stocklist[i][1]
    company=company.replace("'","")
    print(company,code)
    # cur.execute(sql.format(company,code))
#
# con.commit()
# con.close()

