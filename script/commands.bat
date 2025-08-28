
docker run -d -p 9092:9092 --name broker apache/kafka:latest

docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest

docker build -t retriever-docker -f Retriever/Dockerfile .

docker build -t enricher-docker -f Enricher/Dockerfile .

docker build -t preprocessor-docker -f Preprocessor/Dockerfile .

docker build -t persister-docker -f Persister/Dockerfile .

docker build -t  dataretrieval-docker -f dataretrieval/Dockerfile .


