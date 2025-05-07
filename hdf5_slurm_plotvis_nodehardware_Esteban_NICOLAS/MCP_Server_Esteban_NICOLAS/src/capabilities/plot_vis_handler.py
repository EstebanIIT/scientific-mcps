import pandas as pd
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

def plot_vis_columns(csv_path: str, col_x_name: str = None, col_y_name: str = None):
    """Plots two columns from a CSV file. Default to first two columns if not specified"""
    
    csv_file = Path(csv_path)

    if not csv_file.exists():
        return {
            "file": None, 
            "metadata": {
                "query": csv_path,
                "timestamp": datetime.now().isoformat(),
                "error": f"File not found: {csv_path}",
                "mock_data": False
            }
        }

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        return {
            "file": None,
            "metadata": {
                "query": csv_path,
                "timestamp": datetime.now().isoformat(),
                "error": f"CSV read error: {e}",
                "mock_data": False
            }
        }

    # Use the first two columns as default if no column names are provided
    if col_x_name is None and len(df.columns) > 0:
        col_x_name = df.columns[0]  # First column as X
    if col_y_name is None and len(df.columns) > 1:
        col_y_name = df.columns[1]  # Second column as Y

    # Check if the specified columns exist
    if col_x_name not in df.columns or col_y_name not in df.columns:
        return {
            "file": None,
            "metadata": {
                "query": csv_path,
                "timestamp": datetime.now().isoformat(),
                "error": f"Columns {col_x_name} or {col_y_name} not found in CSV",
                "mock_data": False
            }
        }

    # Create output image path
    output_dir = Path("plots_results")
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_stem = csv_file.stem  # Get just filename without extension
    image_path = output_dir / f"plot_{safe_stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(df[col_x_name], df[col_y_name], label=f"{col_y_name} vs {col_x_name}")
    plt.xlabel(col_x_name)
    plt.ylabel(col_y_name)
    plt.title(f"Plot: {col_y_name} vs {col_x_name}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()

    return {
        "file": str(image_path),
        "metadata": {
            "query": csv_path,
            "timestamp": datetime.now().isoformat(),
            "mock_data": False
        }
    }
