from pathlib import Path
from datetime import datetime

async def list_hdf5_files(path_pattern: str = ""):
    """Simulate listing HDF5 files using pathlib-style interaction with Unix-style paths"""
    
    # Create a mock filesystem structure
    mock_root = Path("/data")
    mock_files = [
        mock_root / "simulations/run_1.hdf5",
        mock_root / "simulations/run_2.hdf5",
        mock_root / "archive/exp_1.hdf5",
        mock_root / "archive/exp_2.hdf5",
        mock_root / "temp/test.hdf5",
        mock_root / "config/settings.json",
        Path("/data/sim_run_123/results_1.hdf5"),
        Path("/data/sim_run_123/results_2.hdf5"),
        Path("/data/sim_run_123/SumUp.txt"),
        Path("/data/sim_run_123/SumUp_2.txt")
    ]
    
    # Convert path_pattern to Path object for consistent handling
    search_path = Path(path_pattern) if path_pattern else Path("/data")
    
    # Simulate glob-style matching, ensuring only HDF5 files and proper substring match
    matched = [
        str(file.as_posix()) for file in mock_files  # Ensure Unix-style path strings
        if file.suffix == ".hdf5" and str(search_path) in str(file)
    ]
    
    # Simulate directory existence check (returns an error if the parent dir isn't found)
    if path_pattern and not any(str(search_path) in str(f.parent) for f in mock_files):
        return {
            "files": [],
            "count": 0,
            "metadata": {
                "query": path_pattern,
                "timestamp": datetime.now().isoformat(),
                "error": f"Directory not found: {path_pattern}",
                "mock_data": True
            }
        }
    
    return {
        "files": matched,
        "count": len(matched),
        "metadata": {
            "query": path_pattern,
            "timestamp": datetime.now().isoformat(),
            "mock_data": True,
            "matched_pattern": f"*{search_path.name}*.hdf5" if search_path.name else "*.hdf5"
        }
    }
