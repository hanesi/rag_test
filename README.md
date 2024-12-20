# rag_test
A simple RAG application that ingests PDF data found in the data folder and then uses Chat GPT to ask questions about it.

OpenAI API key is required for use. Additionally for the `stateful-bot.py` a Pinecone API is required, and an Index in Pinecone needs to be created (though it is free). `stateful-bot-in-mem.py` uses Chroma which is an in memory vector store suitable for smaller test usecases. This bot will chunk and embed the data each time it runs.

Once these tasks have been done and the requirements have been installed, the data can be ingested by running

```
python ingestion.py
```

Which will generate the embeddings for your source data. From here

```
python stateful-bot.py
```

Will bring up the bot. Questions and context is retained until the user inputs "quit". For small data inputs, running 

```
stateful-bot-in-mem.py
```

Will handle everything