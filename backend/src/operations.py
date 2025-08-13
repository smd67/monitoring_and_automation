"""
Simple REST endpoint that implements backend processing for operations A-F.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, List
import pandas as pd
import time
import copy 

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operation(BaseModel):
    is_success: bool

class OperationResult(BaseModel):
    operation: str
    is_success: bool
    timestamp: float
    event_id: int

METRICS: List[OperationResult] = []
EVENT_ID = 0

@app.post("/operation-a/")
def operation_a(op: Operation) -> OperationResult:
    """
    Implementation of operation A

    Parameters
    ----------
    op : Operation
        Parameteers passed to method through REST

    Returns
    -------
    OperationResult
        Object that contains the results of the operation
    """
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="A", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.post("/operation-b/")
def operation_b(op: Operation) -> OperationResult:
    """
    Implementation of operation B

    Parameters
    ----------
    op : Operation
        Parameteers passed to method through REST

    Returns
    -------
    OperationResult
        Object that contains the results of the operation
    """
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="B", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.post("/operation-c/")
def operation_c(op: Operation) -> OperationResult:
    """
    Implementation of operation C

    Parameters
    ----------
    op : Operation
        Parameteers passed to method through REST

    Returns
    -------
    OperationResult
        Object that contains the results of the operation
    """
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="C", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.post("/operation-d/")
def operation_d(op: Operation) -> OperationResult:
    """
    Implementation of operation D

    Parameters
    ----------
    op : Operation
        Parameteers passed to method through REST

    Returns
    -------
    OperationResult
        Object that contains the results of the operation
    """
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="D", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.post("/operation-e/")
def operation_e(op: Operation) -> OperationResult:
    """
    Implementation of operation E

    Parameters
    ----------
    op : Operation
        Parameteers passed to method through REST

    Returns
    -------
    OperationResult
        Object that contains the results of the operation
    """
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="E", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.post("/operation-f/")
def operation_f(op: Operation) -> OperationResult:
    global METRICS
    global EVENT_ID
    result = OperationResult(operation="F", is_success=op.is_success, timestamp=time.time(), event_id=EVENT_ID)
    METRICS.append(result)
    EVENT_ID += 1
    return result

@app.get("/collect/")
def collect_metrics() -> List[OperationResult]:
    """
    Method invoked by telegraf to collect operation metrics

    Returns
    -------
    List[OperationResult]
        A list of results for each processes operation.
    """
    global METRICS
    retval = copy.deepcopy(METRICS)
    METRICS = []
    return retval