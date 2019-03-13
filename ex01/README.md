# FROMとCMDを使ってみる

## 問1-1: Ubuntuのイメージを動かす

ヒント: Dockerfileのビルドと実行の方法

```bash
docker image build -t test .
docker container run -it test
```

## 問1-2: コマンドを変更する

上記コマンドを流した時に，`ls /`が実行されるようにする．

