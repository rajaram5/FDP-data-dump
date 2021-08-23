import FDPClientLDPBased as fdpLdpClient

fdp_url = "https://ejprd.fair-dtls.surf-hosted.nl/wp13-fdp"
fdp = fdpLdpClient.FdpLdpClient(fdp_url)
fdp.create_fdp_data_dump()