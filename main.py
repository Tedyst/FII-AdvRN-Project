import json
from langchain_community.graphs.age_graph import AGEGraph
import urllib.parse
from dataclasses import dataclass
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


database = {
    "dbname": "postgres",
    "host": "localhost",
    "user": "postgres",
    "password": "password",
    "port": "5432"
}


graph = AGEGraph(graph_name="gnd", conf=database, create=True)

