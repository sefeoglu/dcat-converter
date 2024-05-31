import os
import sys
import requests
import xmltodict
import json
import argparse
import configparser

PACKAGE_PARENT = '.'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
PREFIX_PATH = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1]) + "/"

def save_results(data, file_path):
    """write data into json file

    Args:
        data (dict): meta data
    """
    with open(file_path, "w", encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

def crawler(url, file_path,  offset_count, start_number,end):
    """ Collecting the data from the repositories and save the data into a json file

    Args:
        url (str): repository url
        offset_count (int): the number of records in each html page
        start_number (int): starting number of a record.
        end (int): total number of records in the repository
    """
    
    i = start_number - (start_number%offset_count)
    exit = False
    record = []
    
    while exit == False:
        new_url = url+str(i)
        print(new_url)
        html_text = requests.get(new_url).text
        record.append({"start":i, "end":i+offset_count, "meta":html_text})
        i = i + offset_count
        if i > end:
            break
        
    data_dict = dict()

    id = 0
    for publication in record:

        meta_data = xmltodict.parse(publication["meta"])
        print(meta_data)
        for meta_item in meta_data['OAI-PMH']['ListRecords']['record']:
            meta_keys = meta_item.keys()

            if "metadata" in meta_keys:

                if "xMetaDiss:xMetaDiss" in meta_item["metadata"].keys():
                    paper = meta_item['metadata']['xMetaDiss:xMetaDiss'] 
                elif "oai_dc:dc" in meta_item["metadata"].keys():
                    paper = meta_item['metadata']['oai_dc:dc'] 
                data_dict[str(id)] = {"xMetaDiss:xMetaDiss": paper}

                id += 1

    save_results(data_dict, file_path)

# if __name__ == "__main__":
#     #parsing
  
#     config = configparser.ConfigParser()
#     config.read(PREFIX_PATH + 'config.ini')

#     #parameters
#     url = config["CRAWLER"]['api_url']
#     file_path = PREFIX_PATH + config['PATH']['input_path']
#     start_number = int(config["CRAWLER"]["start_number"])
#     offset_count = int(config["CRAWLER"]['offset_count'])
#     end_number = int(config["CRAWLER"]['end_number'])

#     print("The data crawler has been started !")
#     # send the parameters to the crawler
#     crawler(url, file_path, offset_count, start_number, end_number)

#     print("The data crawler is completed.")

