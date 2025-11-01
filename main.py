from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import JSONLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_chroma import Chroma
import pandas as pd

load_dotenv()

llm = init_chat_model(model="gpt-4o-mini")

embed_model = OpenAIEmbeddings(model="text-embedding-3-small")

docs = []

json_doc = JSONLoader(file_path="docs/faq.json",
                       jq_schema=".faqs[]", 
                       text_content=False)

faq_docs = json_doc.load()

csv_doc = CSVLoader(file_path="docs/products.csv")

product_doc = csv_doc.load()


docs.append(faq_docs)
docs.append(product_doc)

docs = [doc for sublist in docs for doc in sublist]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200, 
    add_start_index = True
)

all_splits = text_splitter.split_documents(docs)


vector_store = Chroma(collection_name="chatbot", 
                      embedding_function=embed_model, 
                      persist_directory="./chroma_langchain_db",)

doc_ids = vector_store.add_documents(documents=all_splits)


@tool(response_format="content_and_artifact")
def retrieve_context(query: str): 
    """retrieve info to help answer a query"""
    retrieved_docs = vector_store.similarity_search(query=query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

order_df = pd.read_csv("docs/order_data_50.csv")

@tool
def check_order_status(order_id: str):
    """Check order details such as status, value, or product name by order ID."""
    order = order_df[order_df["order_id"].str.upper() == order_id.upper()]
    if order.empty:
        return f"No order found with ID {order_id}. Please check your order number."
    
    row = order.iloc[0]
    return (
        f"Order {row['order_id']} is currently **{row['order_status']}**.\n"
        f"Product: {row['product_name']}\n"
        f"Order Value: ${row['order_value']}\n"
        f"Available Sizes: {row['available_sizes']}"
    )

tools = [retrieve_context, check_order_status]

with open("system_prompt.txt", "r") as f:
    prompt = f.read()


agent = create_agent(llm, tools = tools, system_prompt = prompt, checkpointer=InMemorySaver())
