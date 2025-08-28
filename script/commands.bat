
docker run -d -p 9092:9092 --name broker apache/kafka:latest

docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest