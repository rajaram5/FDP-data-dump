import FDPClientLDPBased as fdpLdpClient

fdp_url = "http://lumc-beat-covid.fair-dtls.surf-hosted.nl"
fdp = fdpLdpClient.FdpLdpClient(fdp_url)
fdp.create_fdp_data_dump()