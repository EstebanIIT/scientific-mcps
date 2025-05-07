import pytest
from src.capabilities.slurm_handler import submit_slurm_job

#=============================================================================#
#Tool: slurm
#=============================================================================#
@pytest.mark.asyncio
async def test_submit_slurm_job_success():
    """Test successful Slurm job submission"""
    result = await submit_slurm_job("/path/to/script.sh", 4)
    assert "job_id" in result
    assert "status" in result
    assert "details" in result
    assert 100000 <= result["job_id"] <= 999999
    assert result["status"] == "PENDING"
    assert result["details"]["cores"] == 4

@pytest.mark.asyncio
async def test_submit_slurm_job_default_cores():
    """Test submission with default core count"""
    result = await submit_slurm_job("/path/to/script.sh")
    assert result["details"]["cores"] == 1  # Default value

@pytest.mark.asyncio
async def test_slurm_invalid_cores_low():
    """Test invalid core count (too low)"""
    with pytest.raises(ValueError, match="Cores must be between 1 and 32"):
        await submit_slurm_job("/path/to/script.sh", 0)

@pytest.mark.asyncio
async def test_slurm_invalid_cores_high():
    """Test invalid core count (too high)"""
    with pytest.raises(ValueError, match="Cores must be between 1 and 32"):
        await submit_slurm_job("/path/to/script.sh", 33)

@pytest.mark.asyncio
async def test_slurm_missing_script_path():
    """Test missing required script path"""
    with pytest.raises(ValueError, match="Script path is required"):
        await submit_slurm_job("")
