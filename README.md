Paper: https://docs.google.com/document/d/12LuUR2Mi4ivhBKnHRDZNgYdb6ccAJm3ZAzXWZb6d5Is/edit?tab=t.0#heading=h.b2fpywla1a22


```
docker build -t postgres-rn -f Dockerfile.postgres .
docker run -d --name postgres-rn -p 5432:5432 postgres-rn
```

Import gnd.sql
```
cat gnd.sql | docker exec -i postgres-rn psql -U postgres
```
