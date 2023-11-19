from block_observation.common.url import get_url
from block_observation.common.util import optional_dict
from symbolchain.facade.SymbolFacade import SymbolFacade  # type: ignore
from .core import address
from dataclasses import dataclass
from typing import Optional
import requests


@dataclass
class Tx:
    id: str
    type: int
    signer_address: str
    height: int
    recipient_address: Optional[str] = None


def get_tx_by_row_data(tx: dict, height: int, facade: SymbolFacade) -> Tx:
    signer_address: str = address.create_by_public_key(
        facade, tx["transaction"]["signerPublicKey"]
    )

    recipient_address: Optional[str] = optional_dict(
        tx["transaction"], "recipientAddress"
    )

    if recipient_address is not None:
        recipient_address = address.create_by_unresolved_address(recipient_address)

    return Tx(
        id=tx["id"],
        type=tx["transaction"]["type"],
        signer_address=signer_address,
        height=height,
        recipient_address=recipient_address,
    )


def get_query(height: int, page_number: int) -> dict:
    return {
        "height": height,
        "pageNumber": page_number,
        "pageSize": 100,
        "embedded": "true",
    }


def get_transaction_by_block(
    node_uri: str, facade: SymbolFacade, height: int
) -> list[Tx]:
    url: str = get_url(url=node_uri, path="transactions/confirmed")
    first_page: dict[str, dict] = requests.get(url, params=get_query(height, 1)).json()

    if len(first_page["data"]) == 0:
        return []

    transactions: list[Tx] = [
        get_tx_by_row_data(tx, height, facade) for tx in first_page["data"]
    ]

    for i in range(100):
        page = requests.get(url, params=get_query(height, i + 2)).json()
        if len(page["data"]) == 0:
            break

        transactions = transactions + [
            get_tx_by_row_data(tx, height, facade) for tx in page["data"]
        ]

        break

    return transactions
