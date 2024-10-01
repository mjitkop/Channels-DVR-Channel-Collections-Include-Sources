# Channels-DVR-Channel-Collections-Include-Sources
Create a channel collection on a Channels DVR server with channels from the specified sources.

## Usage

python create_collection_from_sources.py [-h] [-i IP_ADDRESS] [-n COLLECTION_NAME] [-p PORT_NUMBER] [-v] source_names [source_names ...]

### Positional Arguments  
#### source_names  
    Name(s) of the source(s) from the server to get channels from. If more than one, separate the names with spaces.  

### Options  
#### -h, --help  
    Show this help message and exit.  

#### -i IP_ADDRESS, --ip_address IP_ADDRESS    
    IP address of the Channels DVR server. Not required. Default: 127.0.0.1.  

#### -n COLLECTION_NAME, --collection_name COLLECTION_NAME  
    Name of the collection. Required when more than one source is specified.  
    Not required when only one source is specified. In this case, the collection name will automatically take the name of the one source by default, unless overwritten with this option.  
    
#### -p PORT_NUMBER, --port_number PORT_NUMBER  
    Port number of the Channels DVR server. Not required. Default: 8089.

#### -v, --version  
    Print the version number and exit the program.  

## Examples

### One source  

On my local Channels DVR server (http://127.0.0.1:8089), I have a source called "PBS" and I want to create a channel 
collection that mirrors this source:

> python create_collection_from_sources.py "PBS"

### Two sources

On my local Channels DVR server, I have two sources for Frndly TV: "Frndly TV (with EPG)" and "Frndly TV (no EPG)". I want to combine them into a single channel collection that I will call "Frndly TV":

> python create_collection_from_sources.py -n "Frndly TV" "Frndly TV (with EPG)" "Frndly TV (no EPG)"
