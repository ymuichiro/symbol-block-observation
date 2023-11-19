# SYMBOl BLOCK OBSERVATION

SYMBOL ブロックチェーンの最新のブロックを監視し、ブロックに含まれる最新のトランザクション情報を検出します。
トランザクションを検出すると、環境変数 `http://localhost:3000/api` 宛に post で以下のようなデータをリアルタイムで送信します。

```json
[
  {
    "id": "655A2EDF389CDNNNNNNNNNNE", 
    "height": 2813129, 
    "recipient_address": "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNY", 
    "signer_address": "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNY", 
    "type": 16724
  }
]
```

## 起動方法

```shell
pip install -r requirements.txt 
python -m block_observation
```

## Contribution

このツールは、オープンソースであり、MIT ライセンスのもとで配布されています。バグの報告や機能の提案などは、GitHub の Issues や Pull requests で受け付けています。このツールに関する質問やフィードバックは、作者のメールアドレスにお送りください。