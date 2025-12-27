import weaviate
from weaviate.connect import ConnectionParams
from weaviate.classes.config import Property, DataType, Configure

def connect_weaviate():
    client = weaviate.WeaviateClient(
        connection_params=ConnectionParams.from_url(
            "http://localhost:8081",
            grpc_port=50051
        )
    )
    client.connect()
    return client

def ensure_collection(client, name="experience_store"):
    if name not in client.collections.list_all():
        client.collections.create(
            name=name,
            vectorizer_config=Configure.Vectorizer.text2vec_transformers(),
            properties=[
                Property(name="text", data_type=DataType.TEXT),
                Property(name="event", data_type=DataType.TEXT),
                Property(name="author", data_type=DataType.TEXT),
                Property(name="type", data_type=DataType.TEXT),
            ]
        )

def insert_record(client, data: dict, name="experience_store"):
    client.collections.get(name).data.insert(data)
