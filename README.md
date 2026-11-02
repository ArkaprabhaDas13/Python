🐍 Python Coding Practice for GenAI Interviews
I've divided the questions into four difficulty levels. We'll progress from basic Python to GenAI-related coding scenarios.
Level 1: Python Fundamentals
Focus: Lists, strings, dictionaries, loops, functions, sets, and comprehensions.
#	Question	Concept
1	Find the second-largest number in a list.	Lists, loops
2	Count the frequency of each character in a string.	Dictionaries
3	Find the first non-repeating character in a string.	Strings, dictionaries
4	Check whether two strings are anagrams.	Strings, sorting
5	Remove duplicates from a list without changing the order.	Lists, sets
6	Find common elements between two lists.	Sets
7	Reverse a string without using [::-1].	Loops
8	Find the most frequent element in a list.	Dictionaries
9	Flatten a nested list.	Lists, loops
10	Use map(), filter(), and lambda to transform a list.	Functional programming


Level 2: Intermediate Python
Focus: Functions, comprehensions, iterators, generators, exception handling, and OOP.
#	Question	Concept
11	Write a function that groups words by their first character.	Dictionaries
12	Find duplicate elements in a list.	Sets
13	Implement your own map() function.	Iterators
14	Write a generator that yields numbers from 1 to N.	Generators, yield
15	Sort a list of dictionaries by a particular key.	Lambda, sorting
16	Merge two dictionaries.	Dictionaries
17	Write a decorator that measures function execution time.	Decorators
18	Create a class representing a document with id, content, and metadata.	OOP
19	Handle invalid JSON using exception handling.	JSON, exceptions
20	Read a JSON file and extract specific fields.	File handling


Level 3: Python for Backend and GenAI
These are particularly relevant to your RAG application.
#	Question	GenAI relevance
21	Given a list of documents, split each document into chunks of 100 words.	Chunking
22	Remove empty documents from a document collection.	Data cleaning
23	Given a list of chunks, attach metadata such as document ID and chunk index.	Metadata extraction
24	Implement cosine similarity between two vectors.	Embeddings
25	Given a query vector and 5 document vectors, find the most similar document.	Vector search
26	Implement Top-K retrieval from similarity scores.	RAG retrieval
27	Merge keyword search results and semantic search results.	Hybrid search
28	Write a function that removes duplicate retrieved chunks.	Retrieval optimization
29	Process documents in batches of 10.	Batch processing
30	Implement a simple retry mechanism when an API request fails.	API reliability


Level 4: Advanced Python and Production Scenarios
These questions help you prepare for more demanding engineering interviews.
#	Question	Concept
31	Implement a simple LRU cache.	Data structures
32	Implement a rate limiter.	Backend engineering
33	Write an asynchronous function using asyncio.	Async programming
34	Process multiple API requests concurrently.	Concurrency
35	Implement a producer-consumer pattern.	Queues, concurrency
36	Create a context manager using __enter__ and __exit__.	Python internals
37	Implement a simple document-processing pipeline.	Pipeline design
38	Handle failures in a multi-step document ingestion pipeline.	Exception handling
39	Implement a basic in-memory vector search system.	RAG
40	Build a simple RAG retrieval function using document chunks and similarity scores.	GenAI