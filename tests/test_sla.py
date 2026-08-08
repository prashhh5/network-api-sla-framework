import pytest
from src.sla_monitor import NetworkSLAMonitor

def test_sla_latency_threshold():
    monitor = NetworkSLAMonitor(timeout_sec=5.0)
    result = monitor.check_endpoint("https://httpbin.org/get")
    
    assert result["healthy"] is True
    assert result["status_code"] == 200
    assert result["latency_ms"] < 2000  # Enforce SLA limit under 2 seconds

def test_sla_failure_handling():
    monitor = NetworkSLAMonitor(timeout_sec=1.0)
    result = monitor.check_endpoint("https://httpbin.org/status/500")
    
    assert result["healthy"] is False
    assert result["status_code"] == 500
  
