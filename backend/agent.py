"""
Git Book ADK Agent
Main agent file using Google Generative AI with function calling (tool use)
"""

import os
import json
from typing import Dict, Any, List
import google.generativeai as genai
from google.generativeai.types import FunctionDeclaration, Tool
from dotenv import load_dotenv
from tools import TOOL_FUNCTIONS

# Load environment variables
load_dotenv()


class GitBookAgent:
    """
    ADK-style agent for answering questions about Git using RAG.
    Uses Gemini with function calling for tool execution.
    """
    
    def __init__(
        self,
        model_name: str = 'gemini-2.5-flash',
        temperature: float = 0.3,
        top_p: float = 0.9,
        top_k: int = 40
    ):
        """
        Initialize the Git Book Agent.
        
        Args:
            model_name (str): Gemini model to use
            temperature (float): Sampling temperature
            top_p (float): Nucleus sampling parameter
            top_k (int): Top-k sampling parameter
        """
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        
        # Configure API
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        
        genai.configure(api_key=api_key)
        
        # Define function declarations for tools
        search_func = FunctionDeclaration(
            name="search_book_content",
            description="Search the Git book content using semantic search. Use this when user asks questions about Git, version control, GitHub, or any topic covered in the book.",
            parameters={
                "type": "OBJECT",
                "properties": {
                    "query": {
                        "type": "STRING",
                        "description": "The user's question or search query"
                    }
                },
                "required": ["query"]
            }
        )
        
        chapter_list_func = FunctionDeclaration(
            name="get_chapter_list",
            description="Get a list of all chapters in the book. Use this when user asks about book structure or wants to know what topics are covered.",
            parameters={
                "type": "OBJECT",
                "properties": {}
            }
        )
        
        tools = Tool(function_declarations=[search_func, chapter_list_func])
        
        # Create model with tools
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=genai.GenerationConfig(
                temperature=self.temperature,
                top_p=self.top_p,
                top_k=self.top_k
            ),
            tools=[tools]
        )
        
        # System instruction
        self.system_instruction = """You are a helpful AI assistant for the book "The Version Control Revolution: Git for Non-Developers".

Your role:
- Answer questions about Git, version control, GitHub, and related topics
- Use the search_book_content tool to find relevant information from the book
- Explain concepts in simple, beginner-friendly language
- Provide practical examples and analogies
- Be encouraging and patient with learners

When a user asks a question:
1. Use the search_book_content tool to find relevant book content
2. Synthesize the information into a clear, helpful answer
3. Add your own explanations to make concepts easier to understand
4. If the question is not covered in the book, say so politely and offer general help

Keep responses concise but complete. Use markdown formatting for readability."""
        
        print(f"✅ Agent initialized with model: {self.model_name}")
    
    
    def execute_tool(self, tool_name: str, tool_args: Dict[str, Any]) -> str:
        """
        Execute a tool function.
        
        Args:
            tool_name (str): Name of the tool to execute
            tool_args (Dict): Arguments for the tool
            
        Returns:
            str: Tool execution result
        """
        if tool_name in TOOL_FUNCTIONS:
            try:
                result = TOOL_FUNCTIONS[tool_name](**tool_args)
                return result
            except Exception as e:
                return f"Error executing {tool_name}: {str(e)}"
        else:
            return f"Unknown tool: {tool_name}"
    
    
    def chat(self, user_message: str) -> str:
        """
        Process a user message and return agent response.
        Uses function calling to execute tools when needed.
        
        Args:
            user_message (str): User's question or message
            
        Returns:
            str: Agent's response
        """
        try:
            # Create chat with system instruction
            chat = self.model.start_chat(enable_automatic_function_calling=False)
            
            # Send user message
            response = chat.send_message(
                f"{self.system_instruction}\n\nUser: {user_message}"
            )
            
            # Check if model wants to use tools
            max_iterations = 5
            iteration = 0
            
            while iteration < max_iterations:
                # Check for function calls
                if response.candidates[0].content.parts[0].function_call:
                    function_call = response.candidates[0].content.parts[0].function_call
                    tool_name = function_call.name
                    tool_args = dict(function_call.args)
                    
                    print(f"🔧 Calling tool: {tool_name}")
                    
                    # Execute the tool
                    tool_result = self.execute_tool(tool_name, tool_args)
                    
                    # Send tool result back to model
                    response = chat.send_message(
                        genai.protos.Content(
                            parts=[genai.protos.Part(
                                function_response=genai.protos.FunctionResponse(
                                    name=tool_name,
                                    response={'result': tool_result}
                                )
                            )]
                        )
                    )
                    
                    iteration += 1
                else:
                    # No more function calls, return final response
                    return response.text
            
            return response.text
            
        except Exception as e:
            return f"Error processing message: {str(e)}"
    
    
    def test_agent(self):
        """
        Test the agent with sample queries.
        """
        print("\n" + "=" * 80)
        print("🧪 TESTING GIT BOOK AGENT")
        print("=" * 80)
        
        test_queries = [
            "What chapters are available in the book?",
            "Explain what Git is and why I should use it",
            "How do I create my first commit?",
            "What is branching in Git?"
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n\n{'='*80}")
            print(f"Test {i}: {query}")
            print("=" * 80)
            
            response = self.chat(query)
            print(f"\n🤖 Agent Response:\n{response}")
            print("\n" + "-" * 80)


def create_agent() -> GitBookAgent:
    """
    Factory function to create a configured Git Book Agent.
    
    Returns:
        GitBookAgent: Configured agent instance
    """
    return GitBookAgent(
        model_name='gemini-2.5-flash',
        temperature=0.3,
        top_p=0.9,
        top_k=40
    )


if __name__ == '__main__':
    # Test the agent
    print("Initializing Git Book Agent...")
    agent = create_agent()
    agent.test_agent()
