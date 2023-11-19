import asyncio
import websockets
import json
import requests

from block_observation.symbol.transaction import get_transaction_by_block
from block_observation.common.config import (
    NODE_HTTP_URL,
    NODE_WS_URL,
    NOTIFICATION_HTTP_URL,
)
from block_observation.common.logger import logger
from block_observation.symbol.network import get_network_property
from symbolchain.facade.SymbolFacade import SymbolFacade  # type: ignore


async def block_observation():
    network_props = get_network_property(NODE_HTTP_URL)
    facade = SymbolFacade(network_props.network_type)

    async with websockets.connect(NODE_WS_URL) as websocket:
        async for message in websocket:
            json_message = json.loads(message)

            if "uid" in json_message:
                uid = json_message["uid"]
                logger.info(f"start {network_props.network_type} observation server")
                logger.info(f"uid {uid}")
                await websocket.send(json.dumps({"uid": uid, "subscribe": "block"}))
            else:
                if json_message["topic"] != "block":
                    raise Exception("Invalid block")

                height = json_message["data"]["block"]["height"]

                if type(height) is not str:
                    return Exception("Invalid height type")

                txs = get_transaction_by_block(NODE_HTTP_URL, facade, int(height))

                if len(txs) == 0:
                    logger.info(f"no transactions detected. block height: {height}")
                    continue

                body = [
                    {
                        "id": t.id,
                        "height": t.height,
                        "recipient_address": t.recipient_address,
                        "signer_address": t.signer_address,
                        "type": t.type,
                    }
                    for t in txs
                ]

                for tx in body:
                    logger.info(f"new transactions detected: {json.dumps(tx)}")

                requests.post(
                    NOTIFICATION_HTTP_URL,
                    json=body,
                    headers={"Content-Type": "application/json"},
                )


loop = asyncio.new_event_loop()
loop.run_until_complete(block_observation())
try:
    loop.run_forever()
finally:
    loop.close()
