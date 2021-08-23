from rdflib import Graph, URIRef
import requests
import rdflib

class FdpLdpClient:
    """
    LDP client to interact with FDP. This version of client has functionality to create data dump from FDP.
    """

    def __init__(self, fdp_url):
        self.FDP_URL = fdp_url
        print("FDP URL >>> " + self.FDP_URL)
        self.GRAPH = rdflib.ConjunctiveGraph()

    def create_fdp_data_dump(self):
        """
        Query FDP to retrieve its content and store it in a file. This method uses ldp:contains to navigate through
        different layers.
        """
        urls_to_index = [self.FDP_URL]
        while len(urls_to_index) > 0:
            children_urls = []
            for url in urls_to_index:
                response = requests.request("GET", url)
                if response.status_code == 200:
                    self.__load_to_graph__(url)
                    graph = Graph()
                    graph.parse(url)
                    query = graph.query("""SELECT DISTINCT ?url WHERE {?s <http://www.w3.org/ns/ldp#contains> ?url.}""")
                    for row in query:
                        children_urls.append(row[0])
            urls_to_index.clear()
            urls_to_index = children_urls
        # Store the FDP content
        print("{} statements retrieved from fdp {}.".format(len(self.GRAPH), self.FDP_URL))
        dump_file = open("fdp_dump.nq", "w")
        dump_file.write(self.GRAPH.serialize(format="nquads").decode("utf-8"))
        dump_file.close()

    def __load_to_graph__(self, url):
            """
            Load content of a url into graph
            :param url: Content url
            """
            print("Load content of : " + url)
            graph_ctx = Graph(self.GRAPH.store, URIRef(url))
            graph_ctx.load(url)
