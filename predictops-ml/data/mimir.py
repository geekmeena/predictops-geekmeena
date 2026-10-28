import time

import requests


def query_mimir(promql, mimir_url):
    end = int(time.time())
    start = end - 600

    response = requests.get(
        f"{mimir_url}/prometheus/api/v1/query_range",
        params={
            "query": promql,
            "start": start,
            "end": end,
            "step": 30,
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
