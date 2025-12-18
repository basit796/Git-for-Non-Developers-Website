# 🚀 Git for Non-Developers Website

An interactive educational website designed to help non-developers learn Git through an AI-powered assistant. The website features an intelligent agent that uses embeddings to provide context-aware responses to user questions about Git.

## ✨ Features

- **🤖 AI-Powered Agent**: Interactive chat interface with an intelligent assistant that answers Git-related questions
- **📚 Context-Aware Responses**: Uses embeddings to find relevant information from a comprehensive Git knowledge base
- **💬 Real-time Chat**: Beautiful, responsive chat interface for seamless interaction
- **🎨 Modern UI**: Clean, gradient-based design with a focus on user experience
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## 🏗️ Architecture

The website is built with a simple yet effective architecture:

### Frontend
- **HTML/CSS/JavaScript**: Pure vanilla JavaScript for the interactive UI
- **Responsive Design**: Mobile-first approach with modern CSS
- **Real-time Updates**: Asynchronous communication with the backend

### Backend
- **Node.js + Express**: RESTful API server
- **Embedding Service**: Retrieves relevant context based on user queries
- **Agent Service**: Generates context-aware responses using retrieved information
- **Knowledge Base**: Comprehensive Git documentation stored as embeddings

### Key Components

1. **Embedding System** (`src/embeddings/`):
   - `gitKnowledge.js`: Knowledge base with Git concepts and explanations
   - `embeddingService.js`: Service that finds relevant context using similarity matching

2. **Agent System** (`src/agent/`):
   - `agentService.js`: Generates intelligent responses using context from embeddings

3. **API Routes** (`src/routes/`):
   - `agentRoutes.js`: REST endpoints for agent interactions

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/basit796/Git-for-Non-Developers-Website.git
cd Git-for-Non-Developers-Website
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file (optional):
```bash
cp .env.example .env
```

4. Start the server:
```bash
npm start
```

5. Open your browser and navigate to:
```
http://localhost:3000
```

## 📖 Usage

### Web Interface

1. Open the website in your browser
2. Type your Git-related question in the chat input
3. Press Enter or click "Send"
4. The agent will retrieve relevant context and provide an informative response

### API Endpoints

#### POST /api/agent
Ask a question to the agent.

**Request:**
```json
{
  "query": "What is a Git commit?"
}
```

**Response:**
```json
{
  "success": true,
  "response": "Based on what I know about Git...",
  "timestamp": "2025-12-18T14:14:30.035Z"
}
```

#### GET /api/topics
Get all available topics in the knowledge base.

**Response:**
```json
{
  "success": true,
  "topics": ["What is Git", "Git Repository", "Git Commit", ...],
  "count": 15
}
```

#### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "success": true,
  "status": "healthy",
  "timestamp": "2025-12-18T14:14:30.035Z"
}
```

## 🧪 How It Works

1. **User Input**: User types a question about Git
2. **Query Processing**: The query is sent to the backend API
3. **Context Retrieval**: The embedding service finds relevant information from the knowledge base using similarity matching
4. **Response Generation**: The agent service generates a contextual response based on the retrieved information
5. **Display**: The response is displayed in the chat interface

## 🎯 Knowledge Base Topics

The agent has knowledge about:
- What is Git
- Git Repository
- Git Commit
- Git Branch
- Git Merge
- Git Clone
- Git Pull and Push
- Staging Area
- Git Status
- Git Diff
- Git Log
- Git Remote
- Git Reset
- Git Stash
- Git Ignore

## 🔧 Development

### Project Structure

```
Git-for-Non-Developers-Website/
├── public/                 # Frontend files
│   ├── index.html         # Main HTML file
│   ├── styles.css         # Styles
│   └── app.js             # Frontend JavaScript
├── src/
│   ├── agent/             # Agent service
│   │   └── agentService.js
│   ├── embeddings/        # Embedding system
│   │   ├── gitKnowledge.js
│   │   └── embeddingService.js
│   └── routes/            # API routes
│       └── agentRoutes.js
├── server.js              # Main server file
├── package.json
├── .env.example
├── .gitignore
└── README.md
```

### Adding New Knowledge

To add new topics to the knowledge base, edit `src/embeddings/gitKnowledge.js`:

```javascript
{
    id: 16,
    topic: "Your New Topic",
    content: "Detailed explanation of the topic..."
}
```

## 🚀 Future Enhancements

- Integration with OpenAI API for more sophisticated responses
- Vector database for true semantic search
- User authentication and conversation history
- Multi-language support
- Interactive Git command simulator
- Video tutorials integration

## 📝 License

ISC

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.