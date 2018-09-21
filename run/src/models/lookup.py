#!/usr/bin/env python3

def get_lookup(company_name):
    url = 'http://dev.markitondemand.com/modapis/api/v2/lookup/json?input={}'.format(company_name)
    lookup = json.loads(requests.get(url).text)
    listofnames = []
    for dic in lookup:
        listofnames.append((dic['Symbol'],dic['Name']))
        listofnames.append(dic['Name'])
    return listofnames