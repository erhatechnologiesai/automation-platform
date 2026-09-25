from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import PlatformTenant, WorkflowExecutionRequest, PlatformExecutionReceipt
from app.services.platform_core import execute_platform_service, MODULE_CATALOG

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="The Flagship Unified SaaS Platform combining AI Agents, RAG Pipelines, Workflows, and Tool Calling."
)

@app.get("/")
def platform_root():
    return {
        "platform": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "edition": settings.PLATFORM_EDITION,
        "available_modules": MODULE_CATALOG,
        "status": "ONLINE"
    }

@app.post("/execute", response_model=PlatformExecutionReceipt)
def execute_workflow(req: WorkflowExecutionRequest):
    if req.workflow_module not in MODULE_CATALOG:
        raise HTTPException(status_code=400, detail=f"Invalid module. Supported modules: {list(MODULE_CATALOG.keys())}")
        
    e_id, status, dur, out = execute_platform_service(req.tenant_id, req.workflow_module, req.payload)
    return PlatformExecutionReceipt(
        execution_id=e_id,
        tenant_id=req.tenant_id,
        workflow_module=req.workflow_module,
        status=status,
        execution_time_ms=dur,
        output=out
    )
