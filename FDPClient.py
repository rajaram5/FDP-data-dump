from rdflib import Graph, URIRef
import requests
import rdflib

class FDPClient:

    def __init__(self, fdp_url):
        self.FDP_URL = fdp_url
        print("FDP URL >>> " + self.FDP_URL)
        self.GRAPH = rdflib.ConjunctiveGraph()



    def create_fdp_dump(self):
        self.__add__fdp_content__()
        self.__add__catalog_content__()
        self.__add__dataset_content__()
        self.__add__distribution_content__()
        self.__add__biobank_content__()
        self.__add__patient_registry_content__()

        return self.GRAPH

    def __add__fdp_content__(self):
        self.__load_to_graph__(self.FDP_URL)

    def __add__catalog_content__(self):
        for catalog in self.GRAPH.objects(None, URIRef("http://www.re3data.org/schema/3-0#dataCatalog")):
            self.__load_to_graph__(catalog)

    def __add__dataset_content__(self):
        for dataset in self.GRAPH.objects(None, URIRef("http://www.w3.org/ns/dcat#dataset")):
            self.__load_to_graph__(dataset)

    def __add__biobank_content__(self):
        for distribution in self.GRAPH.objects(None, URIRef("http://purl.org/biosemantics-lumc/ontologies/dcat-extension/biobank")):
            self.__load_to_graph__(distribution)

    def __add__patient_registry_content__(self):
        for distribution in self.GRAPH.objects(None, URIRef("http://purl.org/biosemantics-lumc/ontologies/dcat-extension/patientRegistry")):
            self.__load_to_graph__(distribution)

    def __add__distribution_content__(self):
        for distribution in self.GRAPH.objects(None, URIRef("http://www.w3.org/ns/dcat#distribution")):
            self.__load_to_graph__(distribution)


    def __load_to_graph__(self, url):
            """
            Load content of a url into graph
            :param url: Content url
            """
            print("Load content of : " + url)

            graph = Graph()
            graph_ctx = Graph(self.GRAPH.store, URIRef(url))
            graph_ctx.load(url)




