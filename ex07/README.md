# docker-composeを使ってみる 

## 問7-1: docker-composeコマンドを使ってnginxとflaskを分けてみる
docker-composeコマンドを使ってnginxとflaskを分けて動かそう．
その際，ホストマシンの`./conf.d`をnginxコンテナの`/etc/nginx/conf.d`にマウントすること．

確認用コマンド
```bash
docker-compose up --build -d
curl localhost:8080
```
