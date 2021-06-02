# lambda-rds_switch
開発環境立ち上げてコンテナに入る
```
docker-compose up -d
docker-compose exec dev ash
```
コンテナ内で
```
/app/entry.sh app.handler
```
のあと、コンテナ外で
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"rds_instance":"start"}'
```
