# AI Agent Customer Support Chatbot

An intelligent AI agent that automates customer support for businesses, providing instant responses while maintaining conversation context. Built to reduce support costs, improve response times, and enhance customer satisfaction through autonomous problem-solving capabilities.

## Use Cases

- **E-commerce Support**: Order status, returns, product questions
- **SaaS Help Desk**: Account issues, feature questions, troubleshooting
- **Service Businesses**: Appointment scheduling, service inquiries
- **General Customer Service**: FAQs, policies, general information


## 🎥 Demo
In this demo I embedded the Agent in a mock ecommerce website to showcase how it works in real time. Here's the site repo:
https://github.com/amvvr1/gocart



https://github.com/user-attachments/assets/1e617f23-e335-4572-acdb-c22d8996cc03




## Business Impact

### Save Time & Money
- **Reduce support costs by 70%+** : One AI agent replaces multiple human agents
- **Instant response times** : No customer waits in queue
- **24/7 availability** : Support never sleeps, no shift coverage needed
- **Scale without hiring** : Handle unlimited conversations simultaneously

### Improve Customer Satisfaction
- **Consistent quality** : Every customer gets the same high-quality support
- **Context-aware conversations** : Remembers previous interactions within the session
- **Multi-capability agent** : Can use tools to solve complex problems autonomously
- **Never loses patience** : Always professional and helpful


## Capabilities

The agent can autonomously:
- Search knowledge bases for policy information
- Query product databases for specifications
- Retrieve order status and tracking information
- Escalate to human agents when necessary
- Provide personalized recommendations
- Handle multi-turn conversations with context
- Handle simultaneous conversations


## Features

- **Conversational Memory**: Maintains context throughout the conversation for natural interactions
- **Semantic Understanding**: Uses embeddings to understand customer intent, not just keywords
- **Knowledge Integration**: Can refer to external knowledge base using RAG
- **Persona Engineering**: Agent adopts specific brand voice and personality through system prompts

## Tech Stack

- **Agent Framework**: LangChain (for agent orchestration and tool management)
- **Language Model**: LangChain Chat Model (powered by OpenAI)
- **Embeddings**: OpenAI Embedding Model
- **Query Engine**: LangChain RAG pipeline
- **Memory System**: LangChain conversation memory
- **API Framework**: FastAPI    
- **Tools**: LangChain tools for extensible agent capabilities



## Getting Started

### Prerequisites

- Python 3.11
- OpenAI API key
- UV package manager (recommended) or pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/amvvr1/demo-chatbot.git
cd support chatbot
```

2. Install dependencies with UV
```bash
uv sync
```


3. Set up environment variables
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the FastAPI application
```bash
uv run uvicorn main:app --reload
```

Or with standard Python:
```bash
uvicorn main:app --reload
```

5. Access the API
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs



Example:
```
Customer: "What's your return policy?"
Agent: "We accept returns within 30 days of purchase..."

Customer: "What about exchanges?"
Agent: "For exchanges within the same 30-day period..." 
# Agent remembers we were discussing returns

Customer: "Can you recommend some perfumes under $100"
Agent: "Certainly! Here are some options for perfumes under $100..." 
# Agent can handle specific product recommendations

Customer: "Can you help me track my order?"
Agent: "Sure, can you provide me with your order ID..." 
# Agent connects to order database and gives real-time order status updates
```




## Use Cases

- **E-commerce Support**: Order status, returns, product questions
- **SaaS Help Desk**: Account issues, feature questions, troubleshooting
- **Service Businesses**: Appointment scheduling, service inquiries
- **General Customer Service**: FAQs, policies, general information




## Contact

- **Email**: scholarammar@gmail.com
