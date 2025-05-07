import pytest
from src.mcp_handlers import handle_mcp_request

@pytest.mark.asyncio
async def test_handle_list_resources():
    result = await handle_mcp_request("mcp/listResources", {})
    assert "resources" in result
    assert "tools" in result
    assert len(result["resources"]) == 1
    assert len(result["tools"]) == 3

@pytest.mark.asyncio
async def test_handle_invalid_method():
    with pytest.raises(ValueError):
        await handle_mcp_request("invalid_method", {})