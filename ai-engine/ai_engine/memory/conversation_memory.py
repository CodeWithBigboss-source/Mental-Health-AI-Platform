from ai_engine.llm.groq_client import generate

class ConversationMemory:
    def __init__(self, max_turns: int = 8):
        self.max_turns = max_turns
        self.messages: list[dict] = []
        self.summary: str = ""

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_turns * 2:
            self._summarize_and_trim()

    def _summarize_and_trim(self):
        to_summarize = self.messages[:-self.max_turns]
        text = "\n".join(f"{m['role']}: {m['content']}" for m in to_summarize)
        prompt = f"Summarize the key facts and emotional context from this conversation in 3-4 sentences:\n\n{text}"
        new_summary = generate(messages=[{"role": "user", "content": prompt}], temperature=0.2)
        self.summary = f"{self.summary}\n{new_summary}".strip()
        self.messages = self.messages[-self.max_turns:]

    def get_context_messages(self, system_prompt: str) -> list[dict]:
        context = [{"role": "system", "content": system_prompt}]
        if self.summary:
            context.append({"role": "system", "content": f"Earlier conversation summary: {self.summary}"})
        context.extend(self.messages)
        return context
