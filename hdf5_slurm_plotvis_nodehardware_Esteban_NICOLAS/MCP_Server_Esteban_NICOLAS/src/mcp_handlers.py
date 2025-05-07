from capabilities.hdf5_handler import list_hdf5_files
from capabilities.slurm_handler import submit_slurm_job
from capabilities.cpu_core_handler import report_cpu_cores
from capabilities.plot_vis_handler import plot_vis_columns

async def handle_mcp_request(method: str, params: dict):
    """Route MCP requests to appropriate handlers"""
    if method == "mcp/listResources":
        return await list_resources()
    elif method == "mcp/callTool":
        return await call_tool(params)
    else:
        raise ValueError(f"Unsupported method: {method}")

async def list_resources():
    """List available resources and tools"""
    return {
        "resources": [
            {
                "name": "hdf5_file_listing",
                "description": "List HDF5 files in directory",
                "type": "data",
                "parameters": {
                    "path_pattern": {
                        "type": "string",
                        "description": "File path patterns that match with HDF5 files"
                    }
                }
            }
        ],
        "tools": [
            {
                "name": "plot_vis_columns",
                "description": "Plots two columns from a CSV file. Default to first two columns if not specified.",
                "type": "execution",
                "parameters": {
                    "cvs_path": {
                        "type": "string",
                        "description": "Path of the cvs file with the columns to plot"
                    },
                    "column x": {
                        "type": "string",
                        "description": "Name of the column to abscissa ",
                        "default": "first column"
                    },
                    "column y": {
                        "type": "string",
                        "description": "Name of the column to ordinate ",
                        "default": "second column"
                    }
                }
            },
            {
                "name": "slurm_job_submission",
                "description": "Submit jobs to Slurm scheduler",
                "type": "execution",
                "parameters": {
                    "script_path": {
                        "type": "string",
                        "description": "Path to the job script"
                    },
                    "cores": {
                        "type": "integer",
                        "description": "Number of cores to request",
                        "default": 1
                    }
                }
            },
            {
                "name": "report_cpu_cores",
                "description": "Report number of CPU available on the system",
                "type": "execution",
                "parameters": {}
            }
        ]
    }


async def call_tool(params: dict):
    """Call specific tools based on parameters"""
    tool_name = params.get("tool")
    
    if tool_name == "hdf5_file_listing":
        return await list_hdf5_files(params.get("path_pattern", ""))
    elif tool_name == "slurm_job_submission":
        return await submit_slurm_job(
            script_path=params["script_path"],
            cores=params.get("cores", 1)
        )
    elif tool_name == "report_cpu_cores":
        return await report_cpu_cores()
    elif tool_name == "plot_vis_columns":
        return await plot_vis_columns(path=params["cvs_path"],
            col_x_name=params.get("column x"),
            col_y_name=params.get("column y"),
            )
    else:
        raise ValueError(f"Unknown tool: {tool_name}")
