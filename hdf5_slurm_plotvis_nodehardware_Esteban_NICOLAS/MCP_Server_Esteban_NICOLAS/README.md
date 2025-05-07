MCP Server Implementation

Name: Esteban Nicolas 
Student ID: A20593170

I. Implemented MCP Capabilities

1 Data Resources
1.1 HDF5 File Listing  
   - Lists mock HDF5 files in a directory structure
   - Parameters: `path_pattern` (optional file path pattern)

2 Tools
2.1 Slurm Job Submission  
   - Simulates job submission to a Slurm scheduler
   - Parameters: `script_path` (required), `cores` (optional, default=1)

2.2 CPU Core Reporting  
   - Reports number of CPU cores available on the system
   - No parameters required

2.3 CSV Visualization  
   - Plots two columns from a CSV file (defaults to first two columns)
   - Parameters: `csv_path` (required), `column x`, `column y` (both optional)

II. Setup Instructions

1. Create virtual environment

uv venv -p python3.10
.venv\Scripts\activate  # On Unix: source .venv/bin/activate  

2. Install dependencies

uv sync
uv lock


3. Environment configuration
The project uses pyproject.toml for dependency management. Key dependencies include:

FastAPI

Uvicorn

Pydantic

Pandas

Matplotlib

Pytest

Pytest-ascyncio

4. Running the MCP Server
 
Start the server
cd src
uvicorn server:app --reload

The server will be available at:

API endpoint: http://localhost:8000/mcp
Health check: http://localhost:8000/health

III Testing
1. Run all tests:

pytest tests/
Run specific test file:

pytest tests/test_capabilities_plot_vis.py
pytest tests/test_capabilities_hdf5.py
pytest tests/test_capabilities_cpu_core.py
pytest tests/test_capabilities_slurm.py
pytest tests/test_mcp_handler.py



2. Example Requests
2.1 List available resources

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"mcp/listResources","id":1}'

2.2 List HDF5 files

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"mcp/callTool","params":{"tool":"hdf5_file_listing","path_pattern":"/data/sim_run_123"},"id":2}'

2.3 Submit Slurm job

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"mcp/callTool","params":{"tool":"slurm_job_submission","script_path":"/jobs/analysis.sh","cores":4},"id":3}'

2.4 Plot CSV columns

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"mcp/callTool","params":{"tool":"plot_vis_columns","csv_path":"data.csv","column x":"time","column y":"temperature"},"id":4}'


IV Implementation Notes

1. Mock Implementations:

  -HDF5 file listing uses a simulated directory structure
  -Slurm job submission generates mock job IDs
  -CPU core reporting uses os.cpu_count()

2. CSV Visualization:

  -Creates plots in a plots_results directory
  -Defaults to first two columns if none specified
  -Returns path to generated PNG file

3. Error Handling:

  -Proper JSON-RPC 2.0 error responses
  -Input validation for all parameters
  -Graceful handling of missing files/invalid paths

GITHUB: https://github.com/EstebanIIT/cs550_MCP.git