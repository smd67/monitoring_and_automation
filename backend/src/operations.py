import requests
from bs4 import BeautifulSoup, Tag, NavigableString

import pprint
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

class OperationResult(BaseModel):
    operation: str
    is_success: bool
    timestamp: float

METRICS: List[OperationResult] = []

@app.get("/operation-a/")
def operation_a() -> OperationResult:
    global METRICS
    result = OperationResult(operation="A", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/operation-b/")
def operation_b() -> OperationResult:
    global METRICS
    result = OperationResult(operation="B", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/operation-c/")
def operation_c() -> OperationResult:
    global METRICS
    result = OperationResult(operation="C", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/operation-d/")
def operation_d() -> OperationResult:
    global METRICS
    result = OperationResult(operation="D", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/operation-e/")
def operation_e() -> OperationResult:
    global METRICS
    result = OperationResult(operation="E", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/operation-f/")
def operation_f() -> OperationResult:
    global METRICS
    result = OperationResult(operation="F", is_success=True, timestamp=time.time())
    METRICS.append(result)
    return result

@app.get("/collect/")
def collect_metrics() -> List[OperationResult]:
    global METRICS
    retval = copy.deepcopy(METRICS)
    METRICS = []
    return retval