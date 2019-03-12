# nginxをインストールしてアプリを動かしてみよう

`ex05` の`Dockerfile` を元にしてnginxをインストールする処理を加えよう．
起動コマンドは`start.sh`に変更すること．

ただし，下記コマンドで`app.py`にアクセスできるようにすること．
```
curl localhost:8080
```

注意事項

`flask.conf`は`/etc/nginx/conf.d/flask.conf`に配置すること．
