import gradio as gr
from case_generator import CaseGenerator
from prompts import get_study_prompt, get_question_prompt

def process_notes(medical_notes, api_key):
    """Process medical notes and generate a case study"""
    if not api_key:
        return "Please provide an API key"
    
    generator = CaseGenerator(api_key)
    case_study = generator.generate_case(medical_notes)
    return case_study

def ask_question(medical_notes, current_discussion, api_key):
    """Generate next question based on the ongoing discussion"""
    if not api_key:
        return "Please provide an API key"
    
    generator = CaseGenerator(api_key)
    next_question = generator.generate_question(medical_notes, current_discussion)
    return next_question

def create_interface():
    """Create and configure the Gradio interface"""
    with gr.Blocks() as interface:
        gr.Markdown("# Medical Case Study Assistant")
        
        with gr.Tab("Generate Case"):
            api_key_input = gr.Textbox(label="API Key", type="password")
            notes_input = gr.Textbox(
                label="Enter Medical Notes",
                placeholder="Paste your de-identified medical notes here...",
                lines=5
            )
            generate_btn = gr.Button("Generate Case Study")
            case_output = gr.Textbox(label="Generated Case Study", lines=10)
            
            generate_btn.click(
                fn=process_notes,
                inputs=[notes_input, api_key_input],
                outputs=case_output
            )
        
        with gr.Tab("Interactive Discussion"):
            discussion_notes = gr.Textbox(label="Case Notes", lines=3)
            current_chat = gr.Textbox(label="Current Discussion", lines=5)
            api_key_discuss = gr.Textbox(label="API Key", type="password")
            ask_btn = gr.Button("Ask Next Question")
            question_output = gr.Textbox(label="Next Question", lines=2)
            
            ask_btn.click(
                fn=ask_question,
                inputs=[discussion_notes, current_chat, api_key_discuss],
                outputs=question_output
            )
    
    return interface
