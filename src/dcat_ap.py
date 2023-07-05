from rdflib import Graph, URIRef, BNode, Literal, Namespace


class dcat_ap(object):

    def __init__(self):
        """
        Dcat-ap converter
        """
        self.graph = Graph()
        self.DCAT = Namespace('http://www.w3.org/ns/dcat#')
        self.DCTERMS = Namespace('http://purl.org/dc/terms/')
        self.FOAF = Namespace('http://xmlns.com/foaf/0.1/')
        self.RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        self.dcatde = Namespace('http://dcat-ap.de/def/dcatde/')
        self.XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
        self.VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
        self.LOCN = Namespace('http://www.w3.org/ns/locn#')
        self.graph.bind('foaf', self.FOAF)
        self.graph.bind('dct', self.DCTERMS)
        self.graph.bind('dcat', self.DCAT)
        self.graph.bind('dcatde', self.dcatde)
        self.graph.bind('rdf', self.RDF)
        self.graph.bind('xsd', self.XSD)
        self.graph.bind('vcard', self.VCARD)
        self.graph.bind('locn', self.LOCN)

    def add_dataset(self, data, catalog_uri):
        """ add dataset to graph

        Args:
            data (_type_): _description_
            catalog_uri (_type_): _description_
        """
        dataset_uri = BNode()
        self.graph.add((dataset_uri, self.RDF.type, self.DCAT.Dataset))
        self.graph.add((catalog_uri, self.DCAT.Dataset, dataset_uri))

        if "dc:title" in data.keys():
            if type(data['dc:title']) is list:
                for title in data['dc:title']:
                    if type(title) is dict:
                        self.add_title(title['#text'], dataset_uri)
                    else:
                        self.add_title(title, dataset_uri)
            elif type(data['dc:title']) is dict:
                self.add_title(data['dc:title']['#text'], dataset_uri)
            else:
                self.add_title(data['dc:title'], dataset_uri)

        
        if "dc:creator" in data.keys():
            if type(data['dc:creator']) is list:
                for creator in data['dc:creator']:
                    if type(creator) is dict:
                        if "#text" in creator.keys():
                            self.add_creator(creator["pc:person"]['pc:name']['pc:foreName']+" "+creator['#text']["pc:person"]['pc:name']['pc:surName'], dataset_uri)
                    else:
                        self.add_creator(creator, dataset_uri)
            elif type(data['dc:creator']) is dict:
                if "#text" in data['dc:creator'].keys():
                    self.add_creator(data['dc:creator']["pc:person"]['pc:name']['pc:foreName']+" "+data['dc:creator']["pc:person"]['pc:name']['pc:surName'], dataset_uri)
            else:
                self.add_creator(data['dc:creator'], dataset_uri)
        
        
        if "dc:subject" in data.keys():
            if type(data['dc:subject']) is list:
                for subject in data['dc:subject']:
                    if type(subject) is dict and "#text" in subject.keys():
                        self.add_subject(subject['#text'], dataset_uri)
                    else:
                        self.add_subject(subject, dataset_uri)
            elif type(data['dc:subject']) is dict and "#text" in data['dc:subject'].keys():
                self.add_subject(data['dc:subject']['#text'], dataset_uri)
            else:
                self.add_subject(data['dc:subject'], dataset_uri)
        
        if "dc:description" in data.keys():
            if type(data['dc:description']) is list:
                for description in data['dc:description']:
                    self.add_description(description, dataset_uri)
            elif type(data['dc:description']) is dict:
                self.add_description(data['dc:description']['#text'], dataset_uri)
            else:
                self.add_description(data['dc:description'], dataset_uri)

        
        if "dc:date" in data.keys():
            if type(data['dc:date']) is list:
               self.add_issued(data['dc:date'][0], dataset_uri)
               self.add_modified(data['dc:date'][1], dataset_uri)
            elif type(data['dc:date']) is dict:
                self.add_issued(data['dc:date']['#text'], dataset_uri)
            else:
                self.add_issued(data['dc:date'], dataset_uri)

        if "dc:type" in data.keys():
            if type(data['dc:type']) is list:
                for type_ in data['dc:type']:
                    self.add_type(type_, dataset_uri)
            elif type(data['dc:type']) is dict:
                self.add_type(data['dc:type']['#text'], dataset_uri)
            else:
                self.add_type(data['dc:type'], dataset_uri)

        if "dc:format" in data.keys():
            if type(data['dc:format']) is list:
                for format_ in data['dc:format']:
                    self.add_format(format_, dataset_uri)
            elif type(data['dc:format']) is dict:
                self.add_format(data['dc:format']['#text'], dataset_uri)
            else:
                self.add_format(data['dc:format'], dataset_uri)
        
        if "dc:rights" in data.keys():
            if type(data['dc:rights']) is list:
                for rights in data['dc:rights']:
                    self.add_rights(rights, dataset_uri)
            elif type(data['dc:rights']) is dict:
                self.add_rights(data['dc:rights']['#text'], dataset_uri)
            else:
                self.add_rights(data['dc:rights'], dataset_uri)
        

        if "dcterms:created" in data.keys():
            if type(data['dcterms:created']) is list:
                for created in data['dcterms:created']:
                    if type(created) is dict:
                        self.add_issued(created['#text'], dataset_uri)
                    else:
                        self.add_issued(created, dataset_uri)
            elif type(data['dcterms:created']) is dict:
                self.add_issued(data['dcterms:created']['#text'], dataset_uri)
            else:
                self.add_issued(data['dcterms:created'], dataset_uri)
        
        if "dcterms:dateSubmitted" in data.keys():
            if type(data["dcterms:dateSubmitted"]) is list:
                for date in data["dcterms:dateSubmitted"]:
                    if type(date) is dict:
                        self.add_modified(date['#text'], dataset_uri)
                    else:
                        self.add_modified(date, dataset_uri)
            elif type(data["dcterms:dateSubmitted"]) is dict:
                self.add_modified(data["dcterms:dateSubmitted"]['#text'], dataset_uri)
            else:
                self.add_modified(data["dcterms:dateSubmitted"], dataset_uri)

        if "ddb:identifier" in data.keys():
            if type(data['ddb:identifier']) is list:
                for identifier in data['ddb:identifier']:
                    if type(identifier) is dict:
                        self.add_identifier(identifier['#text'], dataset_uri)
                    else:
                        self.add_identifier(identifier, dataset_uri)
            elif type(data['ddb:identifier']) is dict:
                self.add_identifier(data['ddb:identifier']['#text'], dataset_uri)
            else:
                self.add_identifier(data['ddb:identifier'], dataset_uri)
        if 'dcterms:abstract' in data.keys():
            if type(data["dcterms:abstract"]) is list:
                for abstract in data["dcterms:abstract"]:
                    self.add_description(abstract['#text'], dataset_uri)
            elif type(data["dcterms:abstract"]) is dict:
                self.add_description(data["dcterms:abstract"]["#text"], dataset_uri)
        

        if "dc:language" in data.keys():
            if type(data['dc:language']) is list:
                for language in data['dc:language']:
                    self.add_language(language, dataset_uri)
            elif type(data['dc:language']) is dict:
                self.add_language(data['dc:language']['#text'], dataset_uri)
            else: 
                self.add_language(data['dc:language'], dataset_uri)
        
        if "dc:identifier" in data.keys():
            if type(data['dc:identifier']) is list:
                for identifier in data['dc:identifier']:
                    self.add_identifier(identifier, dataset_uri)
            elif type(data['dc:identifier']) is dict:
                self.add_identifier(data['dc:identifier']['#text'], dataset_uri)
            else:
                self.add_identifier(data['dc:identifier'], dataset_uri)

    def add_catalog(self, dataset, catalog_uri_text, catalog_title):
        """ add catalog to graph"""

        catalog_uri = URIRef(catalog_uri_text)
        title = catalog_title
        self.graph.add((catalog_uri, self.RDF.type, self.DCAT.Catalog))
        self.graph.add((catalog_uri, self.DCTERMS.title, Literal(title)))
        len_ = len(dataset)
        for i in range(0, len_):
            item = None
            for key in dataset[str(i)].keys():
                item = dataset[str(i)][key]
                if key == "paper" or key == "oai_dc:dc":
                    break
            if item is not None:
                self.add_dataset(item, catalog_uri)
            if i == 1000:
                break
    
    def add_title(self, title, dataset_uri):
        """ add title to dataset
        """
        self.graph.add((dataset_uri, self.DCTERMS.title, Literal(title)))

    def add_creator(self, creator, dataset_uri):
        """ add creator to graph"""
        person_uri = BNode()
        self.graph.add((person_uri, self.RDF.type, self.FOAF.Person))
        self.graph.add((person_uri, self.FOAF.name, Literal(creator)))
        self.graph.add((dataset_uri, self.DCTERMS.creator, person_uri))
    
    def add_subject(self, subject, dataset_uri):
        """add subject to graph
        """
        self.graph.add((dataset_uri, self.DCAT.keyword, Literal(subject)))

    def add_description(self, description, dataset_uri):
        """description to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.description, Literal(description)))

    def add_issued(self, date, dataset_uri):
        """add date to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.issued, Literal(date)))
    
    def add_modified(self, date, dataset_uri):
        """add date to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.modified, Literal(date)))

    def add_type(self, _type_, dataset_uri):
        """add type to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.type, Literal(_type_)))

    def add_format(self, format, dataset_uri):
        """add format to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.format, Literal(format)))

    def add_rights(self, right, dataset_uri):
        """add rights to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.rights, Literal(right)))

    def add_language(self, language, dataset_uri):
        """add language to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.language, Literal(language)))

    def add_identifier(self, identifier, dataset_uri):
        """add identifier to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.identifier, Literal(identifier)))


    def save_graph(self, filepath):
        """save graph to file"""
        self.graph.serialize(destination=filepath, format='pretty-xml')


if __name__ == "__main__":
    dcat = dcat_ap()
    dcat.add_catalog()
    dcat.save_graph()