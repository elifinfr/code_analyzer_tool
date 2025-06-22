# chunker_queries.py

QUERIES_BY_LANGUAGE = {
    "python": {
        "top_level_query": "(function_definition) @toplevel.node\n(class_definition) @toplevel.node",
        "split_query": "(function_definition) @split.node"
    }, # <-- LA VIRGULE EST ESSENTIELLE

    # On utilise la version riche pour TSX, car la grammaire 'typescript' la supportera
    "tsx": {
        "top_level_query": """
            (function_declaration name: (identifier) @name) @toplevel.node
            (class_declaration name: (identifier) @name) @toplevel.node
            (lexical_declaration
                (variable_declarator name: (identifier) @name value: [(arrow_function) (function_expression)])
            ) @toplevel.node
            (export_statement
                declaration: [
                    (function_declaration name: (identifier) @name)
                    (class_declaration name: (identifier) @name)
                    (lexical_declaration
                        (variable_declarator name: (identifier) @name value: (arrow_function))
                    )
                ]
            ) @toplevel.node
        """,
        "split_query": """
            (method_definition name: (property_identifier) @name) @split.node
            (public_field_definition name: (property_identifier) @name) @split.node
        """
    },
}

# Ces lignes à la fin assurent que tout utilise la bonne configuration
QUERIES_BY_LANGUAGE["javascript"] = QUERIES_BY_LANGUAGE["tsx"]
QUERIES_BY_LANGUAGE["jsx"] = QUERIES_BY_LANGUAGE["tsx"]
QUERIES_BY_LANGUAGE["typescript"] = QUERIES_BY_LANGUAGE["tsx"]