import requests
from bs4 import BeautifulSoup

records = ['037', '039', '041', '055', '208', '209', '210', '211', '212', '213', '216', '218', '219', '220', '221', '222', '224', '225', '226', '230', '231', '237', '240', '248', '252', '253', '254', '260', '262', '276', '281', '284', '291', '401', '403', '404', '405', '408', '409', '410', '411', '413', '414', '415', '417', '418', '427', '430', '437', '438', '439', '442', '443', '444', '446', '449', '450', '451', '452', '453', '454', '456', '466', '471', '472', '474', '476', '477', '480', '482', '484', '485']
#records = ['039']
#records = ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '111', '112', '113', '114', '115', '116', '117', '118', '119', '121', '122', '123', '124', '200', '201', '202', '203', '205', '207', '208', '209', '210', '212', '213', '214', '215', '217', '219', '220', '221', '222', '223', '228', '230', '231', '232', '233', '234']
##datake = 100
#
for record in records:
    url = "https://www.physionet.org/cgi-bin/atm/ATM"
    payload = "-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"database\"\r\n\r\nmimicdb\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"rbase\"\r\n\r\n%s/\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"srecord\"\r\n\r\n%s\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"record\"\r\n\r\n%s/%s\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"signal\"\r\n\r\nall\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"annotator\"\r\n\r\nabp\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"tdur\"\r\n\r\ne\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"tfmt\"\r\n\r\ntime/date\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"dfmt\"\r\n\r\nstandard\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"tool\"\r\n\r\nsamples_to_csv\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"nbwidth\"\r\n\r\n1349\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"tstart\"\r\n\r\n0\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"tfinal\"\r\n\r\n\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"sfreq\"\r\n\r\n\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\n*\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntdur\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ndfmt\r\n-----------------------------114782935826962\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntfmt\r\n-----------------------------114782935826962--\r\n" % (record, record, record, record)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept-Language': "en-US,en;q=0.5",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "https://physionet.org/cgi-bin/atm/ATM",
        'Content-Type': "multipart/form-data; boundary=---------------------------114782935826962",
        'Content-Length': "1880",
        'Connection': "close",
        'Upgrade-Insecure-Requests': "1",
        'cache-control': "no-cache",
        'Postman-Token': "2f144788-3f84-4ed5-814b-8388de18ed3f"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    #
    soup = BeautifulSoup(response.text,"html.parser")
    #option = soup.find("select",{"name":"rbase"})
    #print(option.get_text().splitlines())
    
    
    raw_list = soup.find_all("pre")[1].get_text()
    raw_line = raw_list.splitlines()
#    raw_line.pop(0)
    
#    output = "'Time and date','MCL1 ','ABP ','RESP '\n"
    output = ""
    for line in raw_line:
        output+=line.replace("\t",",")+"\n"
    
    f = open ('extracted_csv/%s.csv' % record,"w")
    f.write(output)
    f.close()