"""
Gemini LLM service.
Handles all communication with Google's Gemini models.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from app.utils.config import settings


class GeminiService:
    """
    Wrapper around Google's Gemini model.
    """

    def __init__(self) -> None:

        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=settings.TEMPERATURE,
        )

    def invoke(self, prompt: str) -> str:
        """
        Invoke Gemini with a prompt.

        Parameters
        ----------
        prompt : str
            Prompt sent to Gemini.

        Returns
        -------
        str
            Model response.
        """

        response = self.llm.invoke(prompt)

        return response.content.strip()