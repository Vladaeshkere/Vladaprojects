import requests

valyta_list = []
response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
# print(response.status_code)
response_parse = response.text.split('<td data-label="Офіційний курс"')
# print(response_parse)
for parse_elem in response_parse:
    if parse_elem.startswith('>'):
        # print(parse_elem)
        for parse_elem2 in parse_elem.split('<'):
            # print(parse_elem2)
            if parse_elem2.startswith(">"):
                valyta_list.append(float(parse_elem2.split(">")[1].replace(",", "")))

print('Долар США -', int(valyta_list[7]))
