# syntactic_code_chunker.py

from tree_sitter import Language, Parser, Query
from typing import List, Dict, Any, Optional
import logging
# NOUVEL IMPORT
from chunker_queries import QUERIES_BY_LANGUAGE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SyntacticCodeChunker:
    """
    Un découpeur de code qui utilise Tree-sitter pour diviser le code source
    en fragments syntaxiquement cohérents (fonctions, classes, etc.)
    et enrichit chaque fragment avec des métadonnées.
    """

    def __init__(self, language: Language, max_chunk_chars: int = 2048):
        """
        Initialise le découpeur avec le langage Tree-sitter et la taille maximale des fragments.
        Charge dynamiquement les requêtes appropriées pour le langage fourni.
        """
        self.language = language
        self.parser = Parser()
        self.parser.set_language(language)
        self.max_chunk_chars = max_chunk_chars

        lang_name = language.name
        
        # Récupérer les requêtes pour le langage spécifié
        queries = QUERIES_BY_LANGUAGE.get(lang_name)
        if not queries:
            raise ValueError(f"Aucune requête de découpage n'est définie pour le langage '{lang_name}'. Veuillez les ajouter dans 'chunker_queries.py'.")

        # Compiler les requêtes
        self.top_level_query: Query = self.language.query(queries["top_level_query"])
        self.split_query: Query = self.language.query(queries["split_query"])

    # ... (le reste des méthodes _get_node_name, _extract_chunk_info, chunk_source_code ne changent pas)
    def _get_node_name(self, node) -> Optional[str]:
        # ... (code inchangé)
        return ""

    def _extract_chunk_info(self, node, source_bytes: bytes, file_path: str, chunk_type: str, name: Optional[str] = None) -> Dict[str, Any]:
        # ... (code inchangé)
        return {}

    def chunk_source_code(self, source_code: str, file_path: str) -> List[Dict[str, Any]]:
        # ... (code inchangé)
        return []