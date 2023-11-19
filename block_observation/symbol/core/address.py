from binascii import unhexlify
from symbolchain.facade.SymbolFacade import SymbolFacade  # type: ignore
from symbolchain.sc import PublicKey  # type: ignore
import base64


def create_by_unresolved_address(unresolved_address: str) -> str:
    """
    facade.Address(UnresolvedAddress(address).bytes)
    """
    raw_bytes: bytes = unhexlify(unresolved_address)
    row_address: str = base64.b32encode(raw_bytes + bytes(0)).decode("utf8")[0:-1]
    return row_address


def create_by_public_key(facade: SymbolFacade, public_key: str) -> str:
    row_address: str = facade.network.public_key_to_address(PublicKey(public_key))
    return str(row_address)
