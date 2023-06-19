import pytrends
from urllib.parse import quote
import pandas as pd 
from pytrends.request import TrendReq
import jwt
import pandas as pd
from app.models.input_request import InputRequest
from fastapi import APIRouter, Depends, Request, HTTPException, status, File, UploadFile
from pydantic import ValidationError
from typing import Union, Any
from fastapi.security import HTTPBearer
import app.utils.config as config
import app.utils.utils as utils
from pathlib import Path

reusable_oauth2 = HTTPBearer(scheme_name='Authorization')
def validate_secret_token(request: Request, auth=Depends(reusable_oauth2)) -> Union[str, Any]:
    try:
        return True
        # if auth is not None:
        #     if str(auth.credentials).strip() == config.SECRET_KEY.strip():
        #         return True
        #     else:
        #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authenticate Fail")
        # else:
        #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization is not valid")

    except (jwt.PyJWTError, ValidationError) as exc:
        print(exc)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authenticate Fail")

router = APIRouter()

@router.post("/api/v1/keyword_suggestion", response_model_exclude_none=True, dependencies=[Depends(validate_secret_token)])
async def solve_1(input_request: InputRequest):
    global count
    # print(request.client.host)
    keyword = input_request.keyword
    try:
        output = utils.keyword_suggestion(keyword)
        return output
    except HTTPException as e:
        raise e
    
# @router.post("/api/v1/input_file/keywords_cluster", response_model_exclude_none=True, dependencies=[Depends(validate_secret_token)])
# async def solve_1(file: UploadFile=File(...)):
#     global count
#     try:
#         data = await file.read()
#         filename = Path(file.filename).name
#         with open(f"upload_file/{filename}", "wb") as f:
#             f.write(data)
#         try:
#             keywords = list(pd.read_excel(f'upload_file/{filename}')['keywords'].values)
#             output = utils.cluster_keywords(keywords)
#             return output
#         except:
#             raise HTTPException(status_code=400, detail="File chưa đúng định dạng yêu cầu!!!")
#     except HTTPException as e:
#         raise e

