import sys
import os
from utils import read_json
from dcat_ap import dcat_ap
import configparser
from data_crawler import crawler
PACKAGE_PARENT = '.'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
PREFIX_PATH = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1]) + "/"

class converterService(object):

    def __init__(self, catalog_title, catalog_uri, input_path,  out_path):
        """ Convert the json file to rdf file
        
        Args:
        
            catalog_title (str): title of the catalog
            catalog_uri (str): uri of the catalog
            input_path (str): path of the json file
            out_path (str): path of the rdf file
        """

        self.data = read_json(input_path)
        self.catalog_title = catalog_title
        self.catalog_uri = catalog_uri
        self.out_path = out_path
        self.convert()


    def convert(self):
        """ Convert the json file to rdf file
        """
        dcat_ap_ins = dcat_ap(self.out_path)
        # data_item = self.data["0"]['publication']['oai_dc:dc']
        dcat_ap_ins.add_catalog(self.data, self.catalog_uri, self.catalog_title )
   


if __name__ == '__main__':
    #parameters


    print("The data crawler is completed.")
    
    for config_name in os.listdir(PREFIX_PATH+"configs"):
        if config_name.endswith(".ini"):
            config = configparser.ConfigParser()
            url = config["CRAWLER"]['api_url']
            file_path = PREFIX_PATH + config['PATH']['input_path']
            offset_count = int(config["CRAWLER"]['offset_count'])
            end_number = int(config["CRAWLER"]['end_number'])

            print("The data crawler has been started !")
            # send the parameters to the crawler
            crawler(url, file_path, offset_count, end_number)
            print("Start converting json to rdf")
            config.read(PREFIX_PATH + "configs/"+config_name)
            print(config_name)
            # # get the catalog information from config.ini
            catalog_title = PREFIX_PATH + config['REPOSITORY']['repository_name']
            catalog_uri = PREFIX_PATH + config['REPOSITORY']['repository_URI']
            input_path = PREFIX_PATH + config['PATH']['input_path']
            out_catalog_path = PREFIX_PATH + config['RDF']['data_output']

            service = converterService(catalog_title, catalog_uri, input_path, out_catalog_path)
            
    print("Finish converting json to rdf")