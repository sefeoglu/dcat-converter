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

    @staticmethod
    def add_dataset(self, data, catalog_uri):
        """ add dataset to graph

        Args:
            data (_type_): _description_
            catalog_uri (_type_): _description_
        """
        dataset_uri = URIRef(data['uri'])
        self.graph.add((dataset_uri, self.RDF.type, self.DCAT.Dataset))
        self.graph.add((dataset_uri, self.DCTERMS.title, Literal("Dataset 1")))
        self.graph.add((catalog_uri, self.DCAT.Dataset, dataset_uri))

        if "title" in data.keys():
            for title in data['title']:
                self.add_title(title, dataset_uri)
        if "creator" in data.keys():
            for creator in data['creator']:
                self.add_creator(creator, dataset_uri)
        if "subject" in data.keys():
            for subject in data['subject']:
                self.add_subject(subject, dataset_uri)

        if "description" in data.keys():
            for description in data['description']:
                self.add_description(description, dataset_uri)
        if "date" in data.keys():
            for date in data['date']:
                self.add_date(date, dataset_uri)
        if "type" in data.keys():
            for type_ in data['type']:
                self.add_type(type_, dataset_uri)
        if "format" in data.keys():
            for format_ in data['format']:
                self.add_format(format_, dataset_uri)
        if "rights" in data.keys():
            for rights in data['rights']:
                self.add_rights(rights, dataset_uri)
        if "language" in data.keys():
            for language in data['language']:
                self.add_language(language, dataset_uri)
        if "identifier" in data.keys():
            for identifier in data['identifier']:
                self.add_identifier(identifier, dataset_uri)

    def add_catalog(self, dataset, catalog_title, catalog_uri):
        """ add catalog to graph"""

        catalog_uri = BNode()
        title = catalog_title
        self.graph.add((catalog_uri, self.RDF.about, Literal(catalog_uri)))
        self.graph.add((catalog_uri, self.RDF.type, self.DCAT.Catalog))
        self.graph.add((catalog_uri, self.DCTERMS.title, Literal(title)))
        for i, item in enumerate(dataset):
            self.add_dataset(item, catalog_uri)
    
    @staticmethod
    def add_title(self, data, dataset_uri):
        """ add title to dataset
        """
        self.graph.add((dataset_uri, self.DCTERMS.title, Literal(data['title'])))

    @staticmethod
    def add_creator(self, data, dataset_uri):
        """ add creator to graph"""
        person_uri = BNode()
        self.graph.add((person_uri, self.RDF.type, self.FOAF.Person))
        self.graph.add((person_uri, self.FOAF.name, Literal(data['creator'])))
        self.graph.add((person_uri, self.FOAF.mbox, Literal(data['creator_email'])))
        self.graph.add((dataset_uri, self.DCTERMS.creator, person_uri))
    
    @staticmethod
    def add_subject(self, data, dataset_uri):
        """add subject to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.subject, Literal(data['subject'])))

    @staticmethod
    def add_description(self, data, dataset_uri):
        """description to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.description, Literal(data['description'])))

    @staticmethod
    def add_date(self, data, dataset_uri):
        """add date to graph
        """
        self.graph.add((dataset_uri, self.DCTERMS.date, Literal(data['date'])))

    @staticmethod
    def add_type(self, data, dataset_uri):
        """add type to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.type, Literal(data['type'])))

    @staticmethod
    def add_format(self, data, dataset_uri):
        """add format to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.format, Literal(data['format'])))

    @staticmethod
    def add_rights(self, data, dataset_uri):
        """add rights to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.rights, Literal(data['rights'])))

    @staticmethod
    def add_language(self, data, dataset_uri):
        """add language to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.language, Literal(data['language'])))

    @staticmethod
    def add_identifier(self, data, dataset_uri):
        """add identifier to graph"""
        self.graph.add((dataset_uri, self.DCTERMS.identifier, Literal(data['identifier'])))


    def save_graph(self, filepath):
        """save graph to file"""
        self.graph.serialize(destination=filepath, format='pretty-xml')
        

if __name__ == "__main__":
    dcat = dcat_ap()
    dcat.add_catalog()
    dcat.save_graph()