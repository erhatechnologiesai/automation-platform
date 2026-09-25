from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class PlatformTenant(BaseModel):
    tenant_id: str
    organization_name: str
    api_key: str
    active_modules: List[str]

class WorkflowExecutionRequest(BaseModel):
    tenant_id: str
    workflow_module: str # 'RAG_ENGINE', 'AGENT_MESH', 'TOOL_DISPATCHER', 'FORM_PROCESSOR'
    payload: Dict[str, Any]

class PlatformExecutionReceipt(BaseModel):
    execution_id: str
    tenant_id: str
    workflow_module: str
    status: str
    execution_time_ms: float
    output: Dict[str, Any]
