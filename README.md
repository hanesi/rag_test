# rag_test
A simple RAG application that ingests PDF data found in the data folder and then uses Chat GPT to ask questions about it.

OpenAI and Pinecone API keys are required for use. Additionally an Index in Pinecone needs to be created (though it is free)

Once these tasks have been done and the requirements have been installed, the data can be ingested by running

```
python ingestion.py
```

Which will generate the embeddings for your source data. From here

```
python stateful-bot.py
```

Will bring up the bot. Questions and context is retained until the user inputs "quit"