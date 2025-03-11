from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import subprocess
from pathlib import Path


#For crew AI
syspath1 = '../build_anything/src/build_anything'
# syspath1 = sys.path.append(str(Path(__file__).resolve().parent.parent / 'build_anything' / 'src' / 'build_anything'))

sys.path.append(syspath1)

from crew import BuildAnythingCrew


app = FastAPI()

# Allow all CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    message = data.get("message", "")
    
    # Dummy response logic
    dummy_response = f"You said: {message}" if message else "No message received."
    inputs = {
        'user_requirement': message
    }
    
    
    # build= BuildAnythingCrew().crew().kickoff(inputs=inputs)
    # build_output = build.to_dict()
    
    script_path = Path(__file__).resolve().parent.parent / 'build_anything' / 'src' / 'build_anything' / 'move_generated_scripts.py'
    start_node_path = Path(__file__).resolve().parent.parent / 'external_sandbox' / 'node_server.sh'
    
    subprocess.run(['python3', str(script_path)], check=True)
    subprocess.run(['bash', str(start_node_path)], check=True)
    
    return JSONResponse(content={"reply": str(dummy_response)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
    
# uvicorn main:app --reload --host 0.0.0.0 --port 8005
