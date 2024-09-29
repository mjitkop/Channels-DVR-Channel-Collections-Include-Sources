# Channels-DVR-Channel-Collections-Include-Sources
 Create channel collections in Channels DVR that include whole sources.

usage: create_collection_from_source.py [-h] [-i IP_ADDRESS] [-p PORT_NUMBER] [-v] source_name

Create a channel collection on a Channels DVR server with channels from the specified source.

positional arguments:
  source_name           Name of the source.

options:
  -h, --help            show this help message and exit
  -i IP_ADDRESS, --ip_address IP_ADDRESS
                        IP address of the Channels DVR server. Not required. Default: 127.0.0.1
  -p PORT_NUMBER, --port_number PORT_NUMBER
                        Port number of the Channels DVR server. Not required. Default: 8089
  -v, --version         Print the version number and exit the program.

If the URL of the Channels DVR server is not specified, the default URL http://127.0.0.1:8089 will be
used. The name of the channel collection will be the same as the source.
