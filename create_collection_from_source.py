"""
Author: Gildas Lefur (a.k.a. "mjitkop" in the Channels DVR forums)

Description: This script creates a channel collection on the specified Channels DVR server and the
             channels included in the collection will mirror the channels from the specified source.

Disclaimer: this is an unofficial script that is NOT supported by the developers of Channels DVR.

Version History:
- 1.0.0: Internal release for testing and inclusion in OliveTin for Channels.
"""

################################################################################
#                                                                              #
#                                   IMPORTS                                    #
#                                                                              #
################################################################################

import argparse, sys
from Collections import create_channel_collection_from_source

################################################################################
#                                                                              #
#                                  CONSTANTS                                   #
#                                                                              #
################################################################################

DEFAULT_PORT_NUMBER = '8089'
LOOPBACK_ADDRESS    = '127.0.0.1'
VERSION             = '1.0.0'

################################################################################
#                                                                              #
#                                 MAIN PROGRAM                                 #
#                                                                              #
################################################################################

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
                description = "Create a channel collection on a Channels DVR server with channels from the specified source.",
                epilog = "If the URL of the Channels DVR server is not specified, the default URL http://127.0.0.1:8089 " + \
                         "will be used.\n" + \
                         "The name of the channel collection will be the same as the source.")

    # Add the input arguments
    parser.add_argument('-i', '--ip_address', type=str, default=LOOPBACK_ADDRESS, \
                        help='IP address of the Channels DVR server. Not required. Default: 127.0.0.1')
    parser.add_argument('-p', '--port_number', type=str, default=DEFAULT_PORT_NUMBER, \
                        help='Port number of the Channels DVR server. Not required. Default: 8089')
    parser.add_argument('-v', '--version', action='store_true', help='Print the version number and exit the program.')
    parser.add_argument('source_name', type=str, help='Name of the source.')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    ip_address        = args.ip_address
    port_number       = args.port_number
    source_name       = args.source_name
    version           = args.version

    # If the version flag is set, print the version number and exit
    if version:
        print(VERSION)
        sys.exit()

    server_url = f'http://{ip_address}:{port_number}'

    print(f'Creating a channel collection with the channels from source "{source_name}" on the Channels DVR server located at {server_url}...')
    create_channel_collection_from_source(server_url, source_name)
    print('Done!')