from groq import Groq
import re
import os
from dotenv import load_dotenv
load_dotenv()
def fetchAI(prompt):

    client = Groq(api_key=os.getenv("api_key"))
    completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=32768,
            top_p=1,
            stream=False,
            stop=None,
        )
    

    res_raw= completion.choices[0].message.content
    lines = res_raw.splitlines()
    cleaned_lines = []

    for line in lines:

        if re.match(r"^\s*\*\*[A-Za-z0-9 _-]+?\*\*\s*:", line):
            continue

        cleaned_line = re.sub(r"^(</?think>)?\s*\*?\s*", "", line, flags=re.IGNORECASE)
    
        cleaned_lines.append(cleaned_line)


    res = "\n".join(cleaned_lines)
    return res