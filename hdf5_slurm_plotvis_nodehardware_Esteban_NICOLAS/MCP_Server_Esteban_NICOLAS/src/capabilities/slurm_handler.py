import random
from datetime import datetime

async def submit_slurm_job(script_path: str, cores: int = 1):
    """Simulate Slurm job submission"""
    if not script_path:
        raise ValueError("Script path is required")
    
    if not 1 <= cores <= 32:
        raise ValueError("Cores must be between 1 and 32")
    
    job_id = random.randint(100000, 999999)
    
    return {
        "job_id": job_id,
        "status": "PENDING",
        "details": {
            "script": script_path,
            "cores": cores,
            "submitted_at": datetime.now().isoformat(),
            "estimated_start": (
                datetime.now().isoformat()
            ),
            "mock_response": True
        }
    }