from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import JSONLoader, CSVLoader
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_chroma import Chroma
import pandas as pd

load_dotenv()

llm = init_chat_model(model="gpt-4o-mini")

embed_model = OpenAIEmbeddings(model="text-embedding-3-small")

json_doc = JSONLoader(file_path="docs/faq.json",
                       jq_schema=".faqs[]", 
                       text_content=False)
faq_docs = json_doc.load()

csv_doc = CSVLoader(file_path="docs/products.csv")
product_doc = csv_doc.load()


faq_store = Chroma(collection_name="faq", embedding_function=embed_model)
product_store = Chroma(collection_name="products", embedding_function=embed_model)


faq_store.add_documents(faq_docs)
product_store.add_documents(product_doc)


@tool
def answer_faq(query: str): 
    """retrieve info to help answer a FAQ related data"""
    retrieved_docs = faq_store.similarity_search(query=query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

@tool
def give_product_info(query: str):
    """search for product information and give product recommendations"""
    retrieved_docs = product_store.similarity_search(query=query, k=5)
    return "\n\n".join(f"{doc.page_content}" for doc in retrieved_docs)


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

tools = [answer_faq, give_product_info, check_order_status]

with open("system_prompt.txt", "r") as f:
    prompt = f.read()


agent = create_agent(llm, tools = tools, system_prompt = prompt, checkpointer=InMemorySaver())
