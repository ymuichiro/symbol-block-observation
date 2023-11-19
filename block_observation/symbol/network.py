import requests
from dataclasses import dataclass
from typing import Literal


@dataclass
class NetworkProperty:
    network_type: Literal["testnet", "mainnet"]


def get_network_property(node_uri: str) -> NetworkProperty:
    """
    Get the network property of a node
    :param node_uri: URI of the node
    :return: Network property of the node
    """
    res = requests.get(node_uri + "/network/properties").json()
    return NetworkProperty(res["network"]["identifier"])
