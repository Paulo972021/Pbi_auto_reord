CATALOG = {
    "COMPARATIVO": {
        "label": "Comparativo",
        "filters": {
            "entrante": {
                "label": "Entrante",
                "values": ["0", "1"],
            },
            "epn_final": {
                "label": "EPN Final",
                "values": ["ALMAVIVA", "BELLINATI", "EMDIA"],
            },
        },
    }
}

TEMPLATES = [
    {
        "template_id": "tpl_001",
        "page": "COMPARATIVO",
        "filters": {
            "entrante": "1",
            "epn_final": "ALMAVIVA",
        },
    },
    {
        "template_id": "tpl_002",
        "page": "COMPARATIVO",
        "filters": {
            "entrante": "0",
            "epn_final": "EMDIA",
        },
    },
]
