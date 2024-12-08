```
docker build -t postgres-rn -f Dockerfile.postgres .
docker run -d --name postgres-rn -p 5432:5432 postgres-rn
```

Import gnd.sql
```
cat gnd.sql | docker exec -i postgres-rn psql -U postgres
```
