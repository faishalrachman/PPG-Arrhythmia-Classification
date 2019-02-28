import requests
from bs4 import BeautifulSoup




records = ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '111', '112', '113', '114', '115', '116', '117', '118', '119', '121', '122', '123', '124', '200', '201', '202', '203', '205', '207', '208', '209', '210', '212', '213', '214', '215', '217', '219', '220', '221', '222', '223', '228', '230', '231', '232', '233', '234']
#datake = 100

for record in records:
    url = "https://www.physionet.org/cgi-bin/atm/ATM"
    #payload = "-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"database\"\r\n\r\nmitdb\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"rbase\"\r\n\r\n"+record+"\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"record\"\r\n\r\n"+record+"\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"signal\"\r\n\r\nall\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"annotator\"\r\n\r\natr\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tdur\"\r\n\r\ne\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tfmt\"\r\n\r\nseconds\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"dfmt\"\r\n\r\nstandard\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tool\"\r\n\r\nshow_rr\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"nbwidth\"\r\n\r\n1903\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tstart\"\r\n\r\n0\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tfinal\"\r\n\r\n\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"sfreq\"\r\n\r\n\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\n*\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntfmt\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ndfmt\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntdur\r\n-----------------------------171942479424484--\r\n"
    payload = "-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"database\"\r\n\r\nmitdb\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"rbase\"\r\n\r\n"+record+"\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"record\"\r\n\r\n"+record+"\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"signal\"\r\n\r\nall\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"annotator\"\r\n\r\natr\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tdur\"\r\n\r\ne\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tfmt\"\r\n\r\nsamples\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"dfmt\"\r\n\r\nstandard\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tool\"\r\n\r\nshow_rr\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"nbwidth\"\r\n\r\n1903\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tstart\"\r\n\r\n0\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"tfinal\"\r\n\r\n\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"sfreq\"\r\n\r\n\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\n*\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntfmt\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ndfmt\r\n-----------------------------171942479424484\r\nContent-Disposition: form-data; name=\".cgifields\"\r\n\r\ntdur\r\n-----------------------------171942479424484--\r\n"
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "no-cache",
        'Origin': "https://www.physionet.org",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "multipart/form-data; boundary=---------------------------171942479424484",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "https://www.physionet.org/cgi-bin/atm/ATM",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        'Postman-Token': "c5b6182c-a95b-41b1-90b3-4ab2a9ded548"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    #
    soup = BeautifulSoup(response.text,"html.parser")
    #option = soup.find("select",{"name":"rbase"})
    #print(option.get_text().splitlines())
    
    
    raw_list = soup.find_all("pre")[1].get_text()
    raw_line = raw_list.splitlines()
    raw_line.pop(0)
    
    output = "t0,b0,t1,b1,sec\n"
    for line in raw_line:
        output+=line.replace("\t",",")+"\n"
    
    f = open (record+".csv","w")
    f.write(output)
    f.close()
