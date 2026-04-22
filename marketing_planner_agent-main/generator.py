from langchain_google_genai import ChatGoogleGenerativeAI
import time

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="AIzaSyCxX-pBVDfEtAilEhFgqPN16yv9Wi4DaFc",
    temperature=0.7
)

def generate_content(prompt):
    for _ in range(3):
        try:
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            error_msg = str(e)
            print("Gemini Error:", error_msg)

            if "invalid" in error_msg.lower():
                return "❌ Invalid API Key (check new key)"

            if "quota" in error_msg.lower():
                return "❌ Quota exceeded"

            if "503" in error_msg:
                time.sleep(2)
                continue

            return f"❌ Error: {error_msg}"

    return "⚠️ Server busy"