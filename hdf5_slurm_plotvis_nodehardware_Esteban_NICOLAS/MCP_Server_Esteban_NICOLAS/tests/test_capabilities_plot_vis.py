import os
import pytest
import pandas as pd
from pathlib import Path
from src.capabilities.plot_vis_handler import plot_vis_columns

#=============================================================================#
#Tool: plot_vis
#=============================================================================#
@pytest.mark.asyncio
async def test_plot_vis_columns_success():
    """Test successful plot generation"""
    
    # Create test DataFrame and save to CSV
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    csv_path = 'test_results.csv'
    df.to_csv(csv_path, index=False)
    
    # Run the plot function
    result = plot_vis_columns(csv_path)

    # Check if the output file is generated
    assert "file" in result
    assert isinstance(result["file"], str)  # Ensure it's a string path
    assert result["file"].endswith(".png")  # Ensure it's a PNG file
    assert Path(result["file"]).exists()  # Ensure the file exists
    assert result["metadata"]["mock_data"] is False

    # Clean up
    os.remove(csv_path)
    os.remove(result["file"])  # Remove the generated plot file

@pytest.mark.asyncio
async def test_plot_vis_columns_missing_file():
    """Test error handling when the file is missing"""
    
    result = plot_vis_columns("non_existent_file.csv")

    assert "file" in result
    assert result["file"] is None
    assert "error" in result["metadata"]
    assert "File not found" in result["metadata"]["error"]
    assert result["metadata"]["mock_data"] is False

@pytest.mark.asyncio
async def test_plot_vis_columns_invalid_csv():
    """Test error handling when there is an issue reading the CSV"""
    
    # Create an invalid CSV file (empty)
    invalid_csv_path = 'invalid_test.csv'
    with open(invalid_csv_path, 'w') as f:
        f.write("not a valid csv content")
    
    result = plot_vis_columns(invalid_csv_path)

    assert "file" in result
    assert result["file"] is None
    assert "error" in result["metadata"]
    assert "Columns not a valid csv content or None not found in CSV" in result["metadata"]["error"]
    assert result["metadata"]["mock_data"] is False

    # Clean up
    os.remove(invalid_csv_path)

@pytest.mark.asyncio
async def test_plot_vis_columns_missing_columns():
    """Test error handling when the specified columns are missing"""
    
    # Create test DataFrame and save to CSV
    data = {
        'X': [1, 2, 3],
        'Y': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    csv_path = 'test_results.csv'
    df.to_csv(csv_path, index=False)
    
    # Run the plot function with invalid column names
    result = plot_vis_columns(csv_path, "A", "B")

    assert "file" in result
    assert result["file"] is None
    assert "error" in result["metadata"]
    assert "Columns A or B not found in CSV" in result["metadata"]["error"]
    assert result["metadata"]["mock_data"] is False

    # Clean up
    os.remove(csv_path)

@pytest.mark.asyncio
async def test_plot_vis_columns_default_columns():
    """Test default column behavior (first two columns in the CSV)"""
    
    # Create test DataFrame and save to CSV
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    csv_path = 'test_results.csv'
    df.to_csv(csv_path, index=False)
    
    # Run the plot function without specifying columns (default to first two columns)
    result = plot_vis_columns(csv_path)

    # Check if the plot was generated with the first two columns (A, B)
    assert isinstance(result["file"], str)  # Ensure it's a string path
    assert result["file"].endswith(".png")  # Ensure it's a PNG file
    assert Path(result["file"]).exists()  # Ensure the file exists
    assert result["metadata"]["mock_data"] is False

    # Clean up
    os.remove(csv_path)
    os.remove(result["file"])  # Remove the generated plot file
