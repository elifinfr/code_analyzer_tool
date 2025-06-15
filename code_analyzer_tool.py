import requests
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool

# L'URL de l'API que vous venez de créer sur votre PC Windows
RAG_API_URL = "http://192.168.1.131:8000/query"

class CodeAnalyzerInput(BaseModel):
    question: str = Field(..., description="The specific question to ask the codebase via the RAG API.")

class CodeAnalyzerTool(BaseTool):
    """
    Custom Tool that sends a question to the remote RAG API and returns the answer.
    """
    name: str = "RemoteCodebaseQueryTool"
    args_schema: BaseModel = CodeAnalyzerInput
    description: str = "Answers questions about the codebase by querying a remote RAG API."

    def _execute(self, question: str):
        print(f"Sending question to RAG API at {RAG_API_URL}: '{question}'")
        try:
            # Prépare les données à envoyer dans le corps de la requête POST
            payload = {"question": question}

            # Envoie la requête HTTP POST
            response = requests.post(RAG_API_URL, json=payload, timeout=120) # Timeout de 2 minutes

            # Vérifie si la requête a échoué (code d'état 4xx ou 5xx)
            response.raise_for_status()

            # Extrait la réponse JSON
            result = response.json()

            # L'API RAG renvoie {"answer": "votre_reponse"} si tout va bien
            # Donc on cherche la clé "answer"
            return result.get("answer", "No answer content received from API or API returned unexpected format.")

        except requests.exceptions.RequestException as e:
            return f"A network error occurred while contacting the RAG API: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"