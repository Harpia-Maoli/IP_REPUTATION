import csv
import requests
import re


class Doc:
    def __init__(self):
        pass

    def pesquisa_IP_cria_manipula_csv(self):
        file1 = open('IPs.txt', 'r')
        Lines = file1.readlines()

        with open('Dados_Reputação_de_IPs.csv', mode='w', newline='') as csv_file:
            fieldnames = ["IP", "VirusTotal", "AbuseIPDB", "IP-OK", "Reputação | Reportes"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for line in Lines:
                VT = ("https://www.virustotal.com/gui/ip-address/{}/detection".format(line.strip()))
                ABUSEIPDB = ("https://www.abuseipdb.com/check/{}".format(line.strip()))
                IPOK = ("https://ipok.com.br/tools.php?tool=blacklist&valor={}".format(line.strip()))
                req = requests.get(ABUSEIPDB)
                req_regex_not_found = re.findall('not found', str(req.text))
                req_regex_reported_number = re.findall('reported\s(\d+)', str(req.text))

                if not req_regex_reported_number:
                    print("O SITE ESTA RECUSANDO SUAS REQUISIÇÕES |RECOMENDADO FAZER DE 30 EM 30 ALVOS|, STATUS: "
                    + str(req.status_code) + " "+ ABUSEIPDB)
                    writer.writerow({"IP": line.strip(), "VirusTotal": VT, "AbuseIPDB": ABUSEIPDB, "IP-OK": IPOK,
                                     "Reputação | Reportes": 'ERROR'})
                else :
                    print(str(line.strip()) + " POSSUI MÁ REPUTAÇÃO, QUANTIDADES DE REPORT: " + str(req_regex_reported_number))
                    req_regex_reported_number_formated = " | " + req_regex_reported_number[0]
                    

                if len(req_regex_not_found) == 0:
                    writer.writerow({"IP": line.strip(), "VirusTotal": VT, "AbuseIPDB": ABUSEIPDB, "IP-OK": IPOK,
                                     "Reputação | Reportes": "Malicioso" + req_regex_reported_number_formated})
                    #time.sleep(2)
                else:
                    writer.writerow({"IP": line.strip(), "VirusTotal": VT, "AbuseIPDB": ABUSEIPDB, "IP-OK": IPOK,
                                     "Reputação | Reportes": "Limpo"})
                    #time.sleep(2)
