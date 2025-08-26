# Reasoning: prompts.py centralises all prompt templates for easy maintenance 
# and mode-specific customisation. System prompt sets the agent's voice and 
# mode behavior. User prompt injects retrieved chunks and question. This allows
# creative prompt strategies as per bonus. Modes are defined to match brief: 
# interview (professional), story (narrative), fast (bullets), humble_brag (confident).

def get_system_prompt(mode):
    base = "You are a personal codex agent representing the candidate. Speak in first person as if you are the candidate. Be authentic, refer to provided context, and answer truthfully."
    if mode == "interview":
        return base + " Keep answers concise, professional, and informative for evaluation."
    elif mode == "story":
        return base + " Use reflective, narrative style with longer stories."
    elif mode == "fast":
        return base + " Respond in bullet points or TL;DR format."
    elif mode == "humble_brag":
        return base + " Be confident and self-promotional, but grounded in facts."
    return base

def get_user_prompt(question, chunks):
    context = "\n\n".join(chunks)
    return f"Context from my documents:\n{context}\n\nQuestion: {question}\nAnswer in my voice based on the context."