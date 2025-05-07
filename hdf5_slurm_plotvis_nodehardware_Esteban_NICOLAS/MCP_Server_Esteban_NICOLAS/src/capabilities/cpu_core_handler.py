import os
from datetime import datetime

async def report_cpu_cores():
    """Return the number of logical CPU cores available on this system."""
    cores = os.cpu_count()
    
    return {
        "cpu_cores": cores,
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "source": "os.cpu_count()",
            "mock_data": True
        }
    }