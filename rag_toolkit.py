from superagi.tools.base_tool import BaseToolkit, BaseTool #
from typing import Type, List #
from code_analyzer_tool import CodeAnalyzerTool # Importez votre outil spécifique

class RagCodeAnalysisToolkit(BaseToolkit): #
    name: str = "Rag Code Analysis Toolkit" #
    description: str = "Toolkit for analyzing codebase using a remote RAG system." #

    def get_tools(self) -> List[BaseTool]: #
        # Retourne une instance de votre outil
        return [CodeAnalyzerTool()]

    def get_env_keys(self) -> List[str]: #
        # Si votre outil avait besoin de variables d'environnement, vous les listeriez ici.
        # Dans votre cas, l'URL est codée en dur dans code_analyzer_tool.py, donc pas besoin ici.
        return []