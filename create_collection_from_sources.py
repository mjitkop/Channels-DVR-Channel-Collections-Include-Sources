"""
Author: Gildas Lefur (a.k.a. "mjitkop" in the Channels DVR forums)

Description: This script creates a channel collection on the specified Channels DVR server and the
             channels included in the collection will mirror the channels from the specified source.

Disclaimer: this is an unofficial script that is NOT supported by the developers of Channels DVR.

Version History:
- 1.0.0: Internal release for testing and inclusion in OliveTin for Channels.
- 2.0.0: Allow more than one channel source for one collection 
- 2.1.0: Use CDVR_Collections now since Collections was renamed
"""

################################################################################
#                                                                              #
#                                   IMPORTS                                    #
#                                                                              #
################################################################################

import argparse, sys
from CDVR_Collections import create_channel_collection_from_sources

################################################################################
#                                                                              #
#                                  CONSTANTS                                   #
#                                                                              #
################################################################################

DEFAULT_IP_ADDRESS  = '127.0.0.1'
DEFAULT_PORT_NUMBER = '8089'
VERSION             = '2.0.0'

################################################################################
#                                                                              #
#                                 MAIN PROGRAM                                 #
#                                                                              #
################################################################################

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
                description = "Create a channel collection on a Channels DVR server with channels from the specified source(s).",
                epilog = "If the URL of the Channels DVR server is not specified, the default URL http://127.0.0.1:8089 " + \
                         "will be used.\n" + \
                         "In the case where only one source is given, the collection name is not required and will automatically " + \
                         "take the name of the source.\n" + \
                         "In the case where more than one source is given, the collection name (-n option) is required.")

    # Add the input arguments
    parser.add_argument('-i', '--ip_address', type=str, default=DEFAULT_IP_ADDRESS, \
                        help='IP address of the Channels DVR server. Not required. Default: 127.0.0.1')
    parser.add_argument('-n', '--collection_name', type=str, default=None, \
                        help='Name of the collection. Required when more than one source is specified.' + \
                             'Not required when only one source is specified. In this case, the collection name will ' + \
                             'automatically take the name of the one source by default, unless overwritten with this option.')
    parser.add_argument('-p', '--port_number', type=str, default=DEFAULT_PORT_NUMBER, \
                        help='Port number of the Channels DVR server. Not required. Default: 8089')
    parser.add_argument('-v', '--version', action='store_true', help='Print the version number and exit the program.')
    parser.add_argument('source_names', nargs='+', help='Name(s) of the source(s) from the server to get channels from.' + \
                                                        'If more than one, separate the names with spaces.')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    collection_name   = args.collection_name
    ip_address        = args.ip_address
    port_number       = args.port_number
    source_names      = args.source_names
    version           = args.version

    print('Inputs:')
    print(f'  Collection name = "{collection_name}"')
    print(f'  IP address      = {ip_address}')
    print(f'  Port number     = {port_number}')
    print(f'  Source name(s)  = {source_names}')
    print(f'  Print version   = {version}\n')

    # If the version flag is set, print the version number and exit
    if version:
        print(f'Version: {VERSION}')
        sys.exit()

    # Sanity check on the arguments
    if not collection_name and len(source_names) > 1:
        print('Since more than one source is given, a collection name is required.')
        sys.exit()

    server_url = f'http://{ip_address}:{port_number}'

    message = 'Creating a collection with the channels from '
    if len(source_names) > 1:
        message += 'sources'
    else:
        message += 'source'
    message += f' {source_names} on the Channels DVR server located at {server_url}...'

    print(message)
    create_channel_collection_from_sources(server_url, collection_name, source_names)
    print('Done!')