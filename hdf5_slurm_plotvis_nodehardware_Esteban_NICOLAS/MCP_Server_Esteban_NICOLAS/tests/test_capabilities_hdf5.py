import pytest
from pathlib import Path
from src.capabilities.hdf5_handler import list_hdf5_files

#=============================================================================#
#Tool: hdf5
#=============================================================================#
@pytest.mark.asyncio
async def test_list_hdf5_files_basic():
    """Test basic HDF5 file listing functionality"""
    result = await list_hdf5_files("/data/simulations/")
    assert "files" in result
    assert "count" in result
    assert "metadata" in result
    assert all(f.endswith(".hdf5") for f in result["files"])
    assert result["count"] == 2  # Expecting run1.hdf5 and run2.hdf5
    assert result["metadata"]["mock_data"] is True

@pytest.mark.asyncio
async def test_list_hdf5_files_specific_run():
    """Test listing files for a specific simulation run"""
    result = await list_hdf5_files("/data/sim_run_123")
    assert len(result["files"]) == 2  # results_1.hdf5 and results_2.hdf5
    assert all("sim_run_123" in f for f in result["files"])

@pytest.mark.asyncio
async def test_list_hdf5_files_nonexistent_path():
    """Test handling of non-existent directories"""
    result = await list_hdf5_files("/nonexistent/path")
    assert result["files"] == []
    assert result["count"] == 0
    assert "error" in result["metadata"]

@pytest.mark.asyncio
async def test_list_hdf5_files_empty_pattern():
    """Test listing with empty pattern (should return all HDF5 files)"""
    result = await list_hdf5_files("")
    assert result["count"] > 0
    assert len(result["files"]) == result["count"]
