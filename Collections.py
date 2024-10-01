"""
Author: Gildas Lefur (a.k.a. "mjitkop" in the Channels DVR forums)

Description: This module provides resources to handle collections on a Channels DVR server.

Disclaimer: this is an unofficial script that is NOT supported by the developers of Channels DVR.

Version History:
- 1.0.0: Internal release for testing and inclusion in OliveTin for Channels.
- 2.0.0: Added support for more than one channel source for a collection
"""

################################################################################
#                                                                              #
#                                   IMPORTS                                    #
#                                                                              #
################################################################################

import requests
from typing import Optional

################################################################################
#                                                                              #
#                                   CLASSES                                    #
#                                                                              #
################################################################################

class ChannelCollection:
    '''Attributes of one channel collection.'''
    def __init__(self, name = None) -> None:
        self.channels = []
        self.name     = name
        self.slug     = ""

    def add_channels_on_server(self, server_url, channels) -> None:
        '''Add the given channels to this collection and update the server.'''
        self.channels.extend(channels)

        self.update(server_url, self.channels)

    def create_on_server(self, server_url, name, channels) -> None:
        '''
        Send a request to the server located at the given URL to create a channel collection with 
        the given name and list of channels.
        Retrieve the slug number from the JSON response and assign it to this collection.
        '''
        url = f'{server_url}/dvr/collections/channels/new'
        payload = {"name": name, "items": channels}

        response = requests.post(url, json=payload)
        response.raise_for_status()

        json_response = response.json()

        self.channels = channels
        self.name     = name
        self.slug     = json_response['slug']

    def get_info_from_server(self, server_url) -> None:
        '''Retrieve the list of channels from the specified server and update the internal variable.'''
        cc = get_one_channel_collection_from_server(server_url, self.name)

        self.channels = cc.channels
        self.slug     = cc.slug

    def remove_channels_on_server(self, server_url, channels) -> None:
        '''Remove the given channels from this collection and update the server.'''
        self.channels = [item for item in self.channels if item not in channels]

        self.update(server_url, self.channels)

    def update(self, server_url, channels) -> None:
        '''Send a request to the Channels DVR to overwrite the list of channels.'''
        url = f'{server_url}/dvr/collections/channels/{self.slug}'
        payload = {"items": channels}

        response = requests.put(url, json=payload)
        response.raise_for_status()

        self.channels = channels

class ChannelSource:
    '''Attributes of one channel source.'''
    def __init__(self) -> None:
        self.name = ""
        self.channel_ids = []

################################################################################
#                                                                              #
#                                  FUNCTIONS                                   #
#                                                                              #
################################################################################

def create_channel_collection_from_sources(server_url, collection_name, source_names) -> None:
    '''
    Create a channel collection on the server such that it contains all the channels specified in the given sources.
    '''
    channel_ids = []

    if len(source_names) == 1:
        # Only one source
        if not collection_name:
            # Collection name not specified so use the name of the source
            collection_name = source_names[0]

    for s_name in source_names:
        source = get_source_from_server(server_url, s_name)

        if not source:
            raise RuntimeError(f'No source with the name "{s_name}" found on the Channels DVR server located at {server_url}!')
        
        channel_ids.extend(source.channel_ids)

    cc = ChannelCollection()
    cc.create_on_server(server_url, collection_name, channel_ids)

def get_all_channel_collections_from_server(server_url) -> list:
    '''
    Send a request to the Channels DVR server specified by its URL and 
    return a list of ChannelCollection objects.
    '''
    channel_collections = []

    url = f'{server_url}/dvr/collections/channels'

    response = requests.get(url)
    response.raise_for_status()

    json_response = response.json()

    for channel_collection in json_response:
        cc = ChannelCollection()

        cc.name     = channel_collection['name']
        cc.slug     = channel_collection['slug']
        cc.channels = channel_collection['items']

        channel_collections.append(cc)

    return channel_collections

def get_one_channel_collection_from_server(server_url, collection_name) -> Optional[ChannelCollection]:
    '''
    Return one ChannelCollection object that contains the attributes of the requested collection name.
    If the channel collection doesn't exist on the server, return None.
    '''
    all_collections = get_all_channel_collections_from_server(server_url)

    for cc in all_collections:
        if cc.name == collection_name:
            return cc
        
    return None

def get_source_from_server(server_url, source_name) -> Optional[ChannelSource]:
    '''
    Check the specified server for a channel source whose name matches the given name.
    If found, return a ChannelSource object.
    If not found, return None.
    '''
    requested_source = None
    url = f'{server_url}/devices'

    response = requests.get(url)
    response.raise_for_status()

    all_sources = response.json()

    for source in all_sources:
        s_name = source['FriendlyName']
        if s_name == source_name:
            cs = ChannelSource()
            cs.name = source_name

            for channel in source['Channels']:
                cs.channel_ids.append(channel['ID'])

            requested_source = cs
            break

    return requested_source