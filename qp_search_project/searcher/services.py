import json
from urllib import request
import requests

#for rest api
repository_url = 'http://10.3.100.22:8080'
restpath = '/rest'
xmlpath = '/xmlui'

def get_communities():
    communities = request.urlopen(repository_url + restpath + '/communities')
    communities_json = communities.read().decode('utf-8')

    communities_load = json.loads(communities_json)
    communities_processed = []
    for dictionary in communities_load:
        if dictionary['name'] and dictionary['name'] != '':
            communities_processed.append(dictionary)
    #print(communities_processed)
    with open("test.json", 'w') as jsonfile:
        text = json.dumps(communities_processed)
        jsonfile.write(text)

    return communities_processed

def get_by_year(cp):
    for dictionary in cp:
        try:
            year = int(dictionary['name'])
            id = dictionary['id']
            print(year)
            #ccj = curr_collections.read().decode('utf-8')
        except:
            year = 0

        if year != 0:
            path = repository_url + dictionary['link'] + '/collections'
            print(path)
            curr_collections = request.urlopen(path)
            curr_json = json.loads(curr_collections.read().decode('utf-8'))
            print(curr_json[0]['handle'])
            path += str(curr_json[0]['id'])
            temp = requests.get(path)
            print(temp)

if __name__ == '__main__':
    get_by_year(get_communities())