import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

class GenerationService:
    def __init__(self):
        self.model = genai.GenerativeModel(model_name="gemini-2.0-flash")

    def format_prompt(self, context_chunks: list[str], user_query: str) -> str:
        """Construct a prompt from retrieved context and user query."""
        context = "\n\n".join(context_chunks)
        prompt = f"""You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{user_query}

Answer:"""
        return prompt

    def generate_response(self, context_chunks: list[str], user_query: str) -> str:
        """Generate response using Gemini model."""
        prompt = self.format_prompt(context_chunks, user_query)

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()

        except Exception as e:
            return "Sorry, I couldn't generate a response."

generation_service = GenerationService()