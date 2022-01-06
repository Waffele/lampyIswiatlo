#!/bin/bash

CONTAINER="admin-mysql_db.1.jhmt04hxq732lvnr76m7ikzlv"

docker cp ./*.sql $CONTAINER:/tmp/BE_180158.sql
docker cp ./create_and_dump.sh $CONTAINER:/tmp/create_and_dump.sh
docker exec -it $CONTAINER  chmod 777 /tmp/create_and_dump.sh
docker exec -it $CONTAINER /bin/sh /tmp/create_and_dump.sh
docker exec -it $CONTAINER  rm /tmp/BE_180158.sql
docker exec -it $CONTAINER  rm /tmp/create_and_dump.sh