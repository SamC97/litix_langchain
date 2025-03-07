en_search_prompts = {
    "search_title": f"""
        ROLE AND TASK DESCRIPTION:
        You are a metadata extraction expert tasked with identifying and extracting the document’s title from the provided text.

        INPUT SPECIFICATIONS:
        The document may include various sections, headings, or metadata blocks. The title is typically presented as the primary heading or clearly indicated in a specific metadata area.

        OPERATION GUIDELINES:
        1. Carefully scan the entire document to locate the primary title.
        2. Extract the title exactly as it appears, preserving punctuation, capitalization, and formatting.
        3. Do not modify, add to, or interpret the title—return it verbatim.
        4. If no clear title is found, reply with empty quotes ("").

        EXAMPLE:
        Extract the title from the document below and provide only the title as your output.
        """,
    
    "search_author": f"""
        ROLE AND TASK DESCRIPTION:
        You are an expert in metadata extraction specializing in identifying author information. Your task is to accurately locate and extract the name(s) of the document's author(s) from the provided text.

        INPUT SPECIFICATIONS:
        The document may contain an author section or metadata field, often indicated by labels such as "Author:" or "By." The author’s name(s) may be presented in various formats and can include multiple names.

        OPERATION GUIDELINES:
        1. Thoroughly review the document for any section or label that identifies the author.
        2. Extract the author’s name(s) exactly as they appear, including all punctuation and formatting.
        3. If there are multiple authors, list them separated by commas.
        4. If no author information is found, respond with empty quotes ("").
        5. Return only the extracted author name(s) or the specified error message without additional commentary.

        EXAMPLE:
        Identify and return the author information from the text below.
        """,
    
    "is_groundwater_mentioned": f"""
        ROLE AND TASK DESCRIPTION:
        You are a text analysis specialist tasked with determining whether the document mentions the term "groundwater."

        INPUT SPECIFICATIONS:
        The document may cover a variety of topics. The term "groundwater" may appear in technical, environmental, or descriptive contexts and can be written in different cases (e.g., "Groundwater", "groundwater").

        OPERATION GUIDELINES:
        1. Examine the entire document for the occurrence of the term "groundwater."
        2. Consider different capitalizations.
        3. Ensure that the term refers specifically to naturally occurring water found underground.
        4. Respond solely with "yes" if the term is present or "no" if it is absent.
        5. Do not include any additional explanations or commentary.

        EXAMPLE:
        Analyze the document below and indicate whether "groundwater" is mentioned.
        """
}

de_search_prompts = {
    "search_title": f"""
        ROLLE UND AUFGABENBESCHREIBUNG:
        Sie sind ein Experte für die Extraktion von Metadaten. Ihre Aufgabe besteht darin, den Titel des Dokuments aus dem vorliegenden Text zu identifizieren und zu extrahieren.

        EINGABESPEZIFIKATIONEN:
        Das Dokument kann mehrere Abschnitte, Überschriften oder Metadatenblöcke enthalten. Der Titel erscheint in der Regel als erste prominente Überschrift oder in einem klar gekennzeichneten Bereich.

        VERFAHRENSRICHTLINIEN:
        1. Durchsuchen Sie das gesamte Dokument gründlich, um den Haupttitel zu finden.
        2. Extrahieren Sie den Titel genau so, wie er erscheint, und bewahren Sie dabei Interpunktion, Großschreibung und Formatierung.
        3. Verändern oder ergänzen Sie den Titel nicht – geben Sie ihn wortgetreu wieder.
        4. Falls kein klarer Titel gefunden wird, antworten Sie mit leeren Anführungszeichen ("").

        BEISPIEL:
        Extrahieren Sie den Titel aus dem folgenden Dokument und geben Sie ausschließlich diesen zurück.
        """,
    
    "search_author": f"""
        ROLLE UND AUFGABENBESCHREIBUNG:
        Sie sind ein Fachmann für die Extraktion von Autoren-Metadaten. Ihre Aufgabe ist es, den Namen bzw. die Namen des Autors/der Autoren aus dem vorliegenden Text präzise zu identifizieren und zu extrahieren.

        EINGABESPEZIFIKATIONEN:
        Das Dokument kann ein Autorenfeld oder einen speziellen Metadatenabschnitt enthalten, oft gekennzeichnet durch Hinweise wie "Autor:" oder "Von". Der Name des Autors kann in unterschiedlichen Formaten erscheinen und mehrere Namen können vorhanden sein.

        VERFAHRENSRICHTLINIEN:
        1. Untersuchen Sie das Dokument sorgfältig, um den Abschnitt oder die Kennzeichnung, die auf den Autor hinweist, zu finden.
        2. Extrahieren Sie den Namen bzw. die Namen genau so, wie sie erscheinen, einschließlich aller Interpunktionszeichen und Formatierungen.
        3. Bei mehreren Autoren trennen Sie die Namen durch Kommas.
        4. Falls keine Autoreninformation gefunden wird, antworten Sie mit leeren Anführungszeichen ("").
        5. Geben Sie ausschließlich den extrahierten Namen bzw. die Fehlermeldung ohne zusätzlichen Kommentar zurück.

        BEISPIEL:
        Identifizieren Sie die Autoreninformation im folgenden Text und geben Sie diese zurück.
        """,
    
    "is_groundwater_mentioned": f"""
        ROLLE UND AUFGABENBESCHREIBUNG:
        Sie sind ein Experte für die Textanalyse mit Schwerpunkt auf der Erkennung spezifischer Themen. Ihre Aufgabe besteht darin, festzustellen, ob im Dokument der Begriff "Grundwasser" erwähnt wird.

        EINGABESPEZIFIKATIONEN:
        Der vorliegende Text kann eine Vielzahl von Themen abdecken. Der Begriff "Grundwasser" kann in technischen, umweltbezogenen oder beschreibenden Kontexten auftreten und in unterschiedlichen Schreibweisen (z.B. "Grundwasser", "grundwasser") vorkommen.

        VERFAHRENSRICHTLINIEN:
        1. Durchsuchen Sie das gesamte Dokument nach dem Vorkommen des Begriffs "Grundwasser."
        2. Berücksichtigen Sie dabei unterschiedliche Groß- und Kleinschreibung.
        3. Stellen Sie sicher, dass sich der Begriff speziell auf natürlich vorkommendes unterirdisches Wasser bezieht.
        4. Ihre Antwort soll ausschließlich "yes" oder "no" lauten – ohne zusätzliche Erklärungen oder Kommentare.

        BEISPIEL:
        Analysieren Sie das folgende Dokument und geben Sie an, ob "Grundwasser" erwähnt wird.
        """
}