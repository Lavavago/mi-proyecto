# mi-proyecto

## Ejecución local
```
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest tests/unit/ -v
pytest tests/unit/ --cov=src --cov-report=term-missing
pytest tests/unit/ --cov=src --cov-report=xml:coverage.xml
```
