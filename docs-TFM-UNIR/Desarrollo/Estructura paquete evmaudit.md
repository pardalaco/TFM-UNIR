```text
evmaudit/
├── README.md                           # Documentación del paquete
├── pyproject.toml                     # Metadatos y dependencias (PEP 517)
├── src/
│   └── evmaudit/                      # Paquete principal
│       ├── __init__.py                # API pública del paquete
│       ├── py.typed                   # Marker PEP 561 (soporte mypy)
│       ├── models.py                  # Finding, FindingGroup, Severity, Category...
│       ├── runner.py                  # run_slither / run_mythril / run_echidna
│       ├── normalizer.py              # normalize_slither / mythril / echidna
│       ├── correlator.py              # correlate_findings, deduplicate, scoring
│       ├── prioritizer.py             # rank_findings, classify_by_category
│       ├── reporter.py                # generate_report (json/md/csv/sarif)
│       └── exceptions.py              # ToolNotFoundError, AnalysisError...
├── tests/
│   ├── test_normalizer.py             # Tests unitarios del normalizador
│   ├── test_correlator.py             # Tests unitarios del correlador
│   └── fixtures/                      # JSONs de salida reales de Slither/Mythril
└── contracts/                         # Contratos .sol vulnerables para evaluación
```
