# test_chunker_poc.py

import os
import logging
from tree_sitter import Language
from syntactic_code_chunker import SyntacticCodeChunker
# On importe le paquet qui nous donne le "ptr"
import tree_sitter_typescript

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TARGET_FILE_PATH = "test_files/LocalServer.ts"
# Le nom du langage, qui doit correspondre à une clé dans chunker_queries.py
TS_LANGUAGE_NAME = 'typescript' 

def run_poc():
    logging.info(f"--- DÉBUT DU POC AVEC L'API MODERNE : Language(ptr, name) ---")

    if not os.path.exists(TARGET_FILE_PATH):
        logging.error(f"Fichier cible introuvable : {TARGET_FILE_PATH}")
        return

    try:
        # LA NOUVELLE MÉTHODE : On passe le pointeur ET le nom
        # ptr = tree_sitter_typescript.language_typescript()
        # name = 'typescript'
        ts_grammar_language = Language(tree_sitter_typescript.language_typescript(), TS_LANGUAGE_NAME)
        
        logging.info(f"Grammaire '{TS_LANGUAGE_NAME}' chargée avec succès via la méthode moderne.")
    except Exception as e:
        logging.error(f"Impossible de charger la grammaire avec la méthode moderne. Erreur : {e}", exc_info=True)
        return

    # Le reste du script est identique
    try:
        with open(TARGET_FILE_PATH, 'r', encoding='utf-8') as f:
            source_code = f.read()
        logging.info(f"Fichier '{os.path.basename(TARGET_FILE_PATH)}' lu avec succès.")

        chunker = SyntacticCodeChunker(
            language=ts_grammar_language, 
            language_name=TS_LANGUAGE_NAME
        )
        
        logging.info(f"Initialisation du chunker avec le jeu de requêtes '{TS_LANGUAGE_NAME}'...")
        chunks = chunker.chunk_source_code(source_code, TARGET_FILE_PATH)
        logging.info(f"--- FIN DU DÉCOUPAGE. {len(chunks)} CHUNKS GÉNÉRÉS. ---")
        
        # Affichage des résultats...
        print("\n" + "="*50)
        print("          RÉSULTATS DU DÉCOUPAGE (API MODERNE)")
        print("="*50 + "\n")
        for i, chunk in enumerate(chunks):
            metadata = chunk['metadata']
            print(f"--- Chunk #{i+1} ---")
            print(f"  Type    : {metadata.get('type', 'N/A')}")
            print(f"  Nom     : {metadata.get('name', 'N/A')}")
            print(f"  Lignes  : {metadata.get('start_line')} - {metadata.get('end_line')}")
            print(f"  Contenu :\n  ```\n  {''.join(chunk['text'].splitlines(keepends=True)[:5])}  ```")
            print("-" * (len(f"--- Chunk #{i+1} ---")) + "\n")

    except Exception as e:
        logging.error(f"Une erreur est survenue lors du découpage. Erreur : {e}", exc_info=True)

if __name__ == '__main__':
    run_poc()