"""
Logos AI Engine Core
Faith-centered Bible intelligence system
"""

import re

class LogosEngine:
    def __init__(self):
        self.identity = "Logos Bible AI"
        self.mission = "Glorify God, honor Scripture, and guide believers in truth"

    def clean_input(self, text):
        return text.strip()

    def detect_bible_reference(self, text):
        pattern = r'([1-3]?\s?[A-Za-z]+)\s?\d+:\d+'
        match = re.search(pattern, text)
        return match.group(0) if match else None

    def response_style(self):
        return {
            "tone": "calm, wise, encouraging",
            "approach": "scripture-first",
            "avoid": ["political bias", "false doctrine", "speculation"]
        }

    def generate_response(self, user_input):
        user_input = self.clean_input(user_input)

        if not user_input:
            return "Please ask a Bible-based question."

        bible_ref = self.detect_bible_reference(user_input)

        if bible_ref:
            return f"Let us explore {bible_ref} in its biblical context."

        if "who is jesus" in user_input.lower():
            return (
                "Jesus Christ is the Son of God, the Savior of the world "
                "(John 3:16, Colossians 1:15–20). He reveals God's love and truth."
            )

        if "pray" in user_input.lower():
            return (
                "Here is a short prayer:\n\n"
                "Lord, guide our hearts in truth. Help us walk in Your Word. Amen."
            )

        return (
            "I will answer based on Scripture, biblical wisdom, and sound doctrine. "
            "Ask a Bible-related question anytime."
        )


if __name__ == "__main__":
    engine = LogosEngine()
    print(engine.generate_response(input("Ask Logos: ")))
