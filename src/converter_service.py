from utils import read_json
from dcat_ap import dcat_ap

class converterServide(object):

    def __init__(self. catalog_title, catalog_uri, out_path):
        self.config = config
        self.data = read_json("tu-depositonce_repo.json")
        self.output = {}
        self.catalog_title = catalog_title
        self.catalog_uri = catalog_uri
        self.convert()
        self.out_path = out_path

    def convert(self):
        dcat_ap = dcat_ap()
        dcat_ap.add_catalog(data, self.catalog_uri, self.catalog_title )
        dcat_ap.save_graph(self.out_path)


if __name__ == '__main__':
    service = converterServide()
    service.convert()
