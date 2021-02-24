###Import typing from Optional
from typing import Optional

###Import fastapi and uvicorn
import fastapi
import uvicorn

###Create a python object app to use for FASTAPI()
app = fastapi.FastAPI()

###Create an index at the root level and return the HTML body below
@app.get('/')
def index():
    ###Define the html body
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<br>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    ###Return the html body as a reponse
    return fastapi.responses.HTMLResponse(content=body)


####Create another endpoint calle /api and return the HTML content from the body
@app.get('/api')
def index():
    ###Create the HTML content for the body
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Boomshakalaka to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    ###Return the HTML content from the body object
    return fastapi.responses.HTMLResponse(content=body)

###Define the /api/calculate path and return the calculations
@app.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    ###If Z == 0 then return that Z cannto be zero
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "ERROR: Z cannot be zero."},
            status_code=400)
    ###Add the Values of x and y together
    value = x + y
    ###If z is not empty/None then return the value divided by z
    if z is not None:
        value /= z
    ###Return the x, y, and z variable along with the value in json format (key value pairs)
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }

