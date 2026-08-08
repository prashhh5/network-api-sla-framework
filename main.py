from src.sla_monitor import NetworkSLAMonitor

TARGET_ENDPOINTS = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/500"
]

def run_health_audit():
    monitor = NetworkSLAMonitor(timeout_sec=3.0)
    print("\n=============================================")
    print("     NETWORK & API SLA MONITORING AUDIT      ")
    print("=============================================\n")
    
    for url in TARGET_ENDPOINTS:
        result = monitor.check_endpoint(url)
        status = "PASS" if result["healthy"] else "FAIL"
        print(f"[{status}] URL: {result['url']}")
        print(f"       Status Code: {result['status_code']} | Latency: {result['latency_ms']} ms")
        if result["error"]:
            print(f"       Error: {result['error']}")
        print("-" * 45)

if __name__ == "__main__":
    run_health_audit()
  
