### Langchain

import os
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
apikey = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Se increvem no canal para aprender python")
]

model = ChatOpenAI(model='gpt-4o')
parser = StrOutputParser()

# response = model.invoke(mensagens)
# text_response = parser.invoke(response)
# print(text_response)

#chain = model | parser ## Cadeia de passos
#text = chain.invoke(mensagens) ## output do modelo + parser -> output da cedeia (considerando o ultima etapa)

template_messages = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto para {idiom}"), #system
    ("user", "{text}"), #user
])

template_messages.invoke({"idiom": "inglês",
                        "text": "eu amo python"})

chain = template_messages | model | parser

## criação do template de mensagens + modelo + parser -> output da cedeia (considerando o ultima etapa)
#text = chain.invoke({"idiom": "inglês", "text": "eu amo python"})
#print(text)
