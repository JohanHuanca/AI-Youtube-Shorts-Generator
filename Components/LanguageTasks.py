from pydantic import BaseModel,Field
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API")

if not api_key:
    raise ValueError("API key not found. Make sure it is defined in the .env file.")

class JSONResponse(BaseModel):
    """
    The response should strictly follow the following structure: -
     [
        {
        start: "Start time of the clip",
        content: "Highlight Text",
        end: "End Time for the highlighted clip"
        }
     ]
    """
    start: float = Field(description="Start time of the clip")
    content: str= Field(description="Highlight Text")
    end: float = Field(description="End time for the highlighted clip")

system = """

Based on the Transcription user provides with start and end, Highilight the main parts in less then 1 min which can be directly converted into a short. highlight it such that its intresting and also keep the time staps for the clip to start and end. only select a continues Part of the video

Follow this Format and return in valid json 
[{{
start: "Start time of the clip",
content: "Highlight Text",
end: "End Time for the highlighted clip"
}}]
it should be one continues clip as it will then be cut from the video and uploaded as a tiktok video. so only have one start, end and content
Make sure that the content's length doesn't go beyond 60 seconds.

Dont say anything else, just return Proper Json. no explanation etc


IF YOU DONT HAVE ONE start AND end WHICH IS FOR THE LENGTH OF THE ENTIRE HIGHLIGHT, THEN 10 KITTENS WILL DIE, I WILL DO JSON['start'] AND IF IT DOESNT WORK THEN...

<TRANSCRIPTION>
{Transcription}

"""

# User = """
# Example
# """




def GetHighlight(Transcription):
    try:
        from langchain_openai import ChatOpenAI
        
        print(f"\n🔑 Verificando API Key...")
        if not api_key or api_key == "tu_api_key_aqui":
            print("❌ Error: API Key de OpenAI no configurada")
            print("📝 Por favor:")
            print("   1. Abre el archivo .env")
            print("   2. Reemplaza 'tu_api_key_aqui' con tu API Key real")
            print("   3. Obtén tu API Key en: https://platform.openai.com/api-keys")
            return 0, 0
        
        print(f"✅ API Key encontrada (primeros 8 caracteres): {api_key[:8]}...")
        print(f"🤖 Conectando con OpenAI GPT-4...")
        
        llm = ChatOpenAI(
            model="gpt-4o-2024-05-13",
            temperature=0.7,
            api_key = api_key
        )

        from langchain.prompts import ChatPromptTemplate
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system",system),
                ("user",Transcription)
            ]
        )
        
        print(f"📊 Analizando transcripción para encontrar el mejor highlight...")
        chain = prompt |llm.with_structured_output(JSONResponse,method="function_calling")
        response = chain.invoke({"Transcription":Transcription})
        
        Start,End = int(response.start), int(response.end)
        print(f"✅ Highlight encontrado: {Start}s - {End}s (duración: {End-Start}s)")
        
        # print(f"Start is {Start}")
        # print(f"End is {End}\n\n")
        if Start==End:
            print("⚠️  Error: Start y End son iguales")
            Ask = input("Error - Get Highlights again (y/n) -> ").lower()
            if Ask == "y":
                Start, End = GetHighlight(Transcription)
            return Start, End
        return Start,End
        
    except Exception as e:
        print(f"\n❌ Error al obtener highlight: {type(e).__name__}")
        print(f"📋 Detalle del error: {str(e)}")
        
        if "AuthenticationError" in str(type(e)):
            print("\n🔑 Error de autenticación con OpenAI:")
            print("   - Verifica que tu API Key sea correcta")
            print("   - Verifica que tengas créditos en tu cuenta de OpenAI")
            print("   - Obtén una nueva key en: https://platform.openai.com/api-keys")
        elif "RateLimitError" in str(type(e)):
            print("\n⏱️  Has excedido el límite de requests de la API")
            print("   - Espera unos minutos e intenta de nuevo")
            print("   - O actualiza tu plan en OpenAI")
        elif "InvalidRequestError" in str(type(e)):
            print("\n⚠️  La transcripción es demasiado larga o tiene formato inválido")
        
        return 0, 0

if __name__ == "__main__":
    print(GetHighlight(User))
