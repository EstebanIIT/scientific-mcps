from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from mcp_handlers import handle_mcp_request

app = FastAPI()
class JSONRPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: dict
    id: str | int | None = None


@app.post("/mcp")
async def mcp_endpoint(request: JSONRPCRequest):
    try:
        if request.jsonrpc != "2.0":
            raise ValueError("Only JSON-RPC 2.0 is supported")
        
        response = await handle_mcp_request(request.method, request.params)
        
        return {
            "jsonrpc": "2.0",
            "result": response,
            "id": request.id
        }
        
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={
                "jsonrpc": "2.0",
                "error": {"message": str(e)},
                "id": request.id
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "error": {"message": str(e)},
                "id": request.id
            }
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
