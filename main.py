import gradio as gr
from interface import create_interface
from case_generator import CaseGenerator

def main():
    """Main function to run the application"""
    # Create the Gradio interface
    interface = create_interface()
    
    # Launch the interface
    interface.launch()

if __name__ == "__main__":
    main()