from openai import OpenAI
from prompts import get_study_prompt, get_question_prompt

class CaseGenerator:
    def __init__(self, api_key):
        """Initialize the CaseGenerator with API key"""
        self.client = OpenAI(api_key=api_key)
    
    def generate_case(self, medical_notes):
        """Generate a case study from medical notes"""
        try:
            prompt = get_study_prompt(medical_notes)
            response = self.client.chat.completions.create(
                model="gpt-4",  # or your preferred model
                messages=[
                    {"role": "system", "content": "You are a medical educator helping students learn from clinical cases."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating case: {str(e)}"
    
    def generate_question(self, medical_notes, current_discussion):
        """Generate the next question based on the discussion"""
        try:
            prompt = get_question_prompt(medical_notes, current_discussion)
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a medical educator guiding a student through case discussion."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating question: {str(e)}"
