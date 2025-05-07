import pytest
from src.capabilities.cpu_core_handler import report_cpu_cores

#=============================================================================#
#Tool: cpu_core
#=============================================================================#
@pytest.mark.asyncio
async def test_report_cpu_cores():
    """Test CPU core reporting with metadata"""
    result = await report_cpu_cores()
    
    assert "cpu_cores" in result
    assert isinstance(result["cpu_cores"], int)
    assert result["cpu_cores"] > 0

    assert "metadata" in result
    assert "timestamp" in result["metadata"]
    assert "source" in result["metadata"]
    assert result["metadata"]["mock_data"] is True
