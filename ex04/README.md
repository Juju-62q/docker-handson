# Dockerのキャッシュ構造を理解する
この2つで何が違うか比べてみよう．

## 問4-1: 先に全ファイルを追加するDockerfileを書いてみる．
`requirements.txt`, `get-docker.py`を先にコンテナに追加して，パッケージをインストールする．
その後`get-docker.py`を実行する．

ヒント: 下記コマンドでパッケージインストールできます！

```bash
pip install -r requirements.txt
```

`get-docker.py` のURLを変更してもう一度実行する．

## 問4-2: 先にパッケージのインストールをして，プログラムを追加するDockerfileを書いてみる
`requirements.txt`を追加して，パッケージのインストールを行う．
その後`get-docker.py` を追加してこれを実行する．

`get-docker.py` を元に戻してもう一度実行する．
次に`requirements.txt`に`urllib3`を追加してもう一度実行する．

