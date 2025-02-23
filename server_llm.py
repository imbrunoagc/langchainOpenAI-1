from code_llm import chain
from fastapi import FastAPI
from langserve import add_routes

# create app
app = FastAPI(title="Meu app de IA", description="Traduza suas ideias para qualquer idioma")


add_routes(app, chain, path="/tradutor")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host='localhost', port=8000) #add o path/playground