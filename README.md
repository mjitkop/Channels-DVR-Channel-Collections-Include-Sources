# Channels-DVR-Channel-Collections-Include-Sources
Create a channel collection on a Channels DVR server with channels from the specified source.

## Usage

python create_collection_from_source.py [-h] [-i IP_ADDRESS] [-p PORT_NUMBER] [-v] source_name

### Positional Arguments  
source_name: Name of the source.  

### Options  
-h, --help: Show this help message and exit.

-i IP_ADDRESS, --ip_address IP_ADDRESS: IP address of the Channels DVR server. Not required. Default: 127.0.0.1.

-p PORT_NUMBER, --port_number PORT_NUMBER: Port number of the Channels DVR server. Not required. Default: 8089.

-v, --version: Print the version number and exit the program.  

If the URL of the Channels DVR server is not specified, the default URL http://127.0.0.1:8089 will be used.  
The name of the channel collection will be the same as the source.

## Example

On my local Channels DVR server (http://127.0.0.1:8089), I have a source called "PBS" and I want to create a channel 
collection that mirrors this source:

python create_collection_from_source.py "PBS"

## Possible future improvements

Create a channel collection with channels from more than one source.
