import FDPClient as fdpClient

#fdp_url = "http://lumc-beat-covid.fair-dtls.surf-hosted.nl"
#fdp_url = "https://fdp.lumc.nl"
fdp_url = "http://localhost:8082"


fdp = fdpClient.FDPClient(fdp_url)
graph = fdp.create_fdp_dump()
print("{} statements retrieved from fdp {}.".format(len(graph), fdp_url))
dump_file = open("fdp_dump.nq", "w")
dump_file.write(graph.serialize(format="nquads").decode("utf-8"))
dump_file.close()