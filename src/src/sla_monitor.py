import time
import requests
from typing import Dict, Any

class NetworkSLAMonitor:
    """Monitors latency, HTTP status codes, and SLA thresholds for network microservices."""
    def __init__(self, timeout_sec: float = 2.0):
        self.timeout = timeout_sec

    def check_endpoint(self, url: str) -> Dict[str, Any]:
        start_time = time.time()
        try:
            response = requests.get(url, timeout=self.timeout)
            latency_ms = round((time.time() - start_time) * 1000, 2)
            return {
                "url": url,
                "status_code": response.status_code,
                "latency_ms": latency_ms,
                "healthy": response.status_code == 200,
                "error": None
            }
        except requests.exceptions.RequestException as e:
            return {
                "url": url,
                "status_code": None,
                "latency_ms": None,
                "healthy": False,
                "error": str(e)
            }
              
