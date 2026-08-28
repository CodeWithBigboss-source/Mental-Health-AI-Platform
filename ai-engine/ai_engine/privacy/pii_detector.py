from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

_analyzer = AnalyzerEngine()
_anonymizer = AnonymizerEngine()

def redact_pii(text: str) -> tuple[str, list[str]]:
    results = _analyzer.analyze(text=text, language="en")
    if not results:
        return text, []
    anonymized = _anonymizer.anonymize(text=text, analyzer_results=results)
    entity_types = list({r.entity_type for r in results})
    return anonymized.text, entity_types
