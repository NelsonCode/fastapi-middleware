from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(CORSMiddleware(allow_origins=["*"]))


@app.middleware("http")
async def verify_user_agent(request: Request, call_next):

    if request.headers['User-Agent'].find("Mobile") == -1:
        response=await call_next(request)
        return response
    else:
        return JSONResponse(content={
            "message": "no permitimos mobiles"
        }, status_code=401)


@ app.get('/')
def index(request: Request, response: Response):
    response.set_cookie(key="mykey", value="Hola")
    return {'message': 'ok'}
