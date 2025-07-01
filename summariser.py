# summariser.py

from transformers import pipeline

# Initialize the summarization pipeline with a Hugging Face model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarise_text(prompt):
    try:
        # Generate the summary with reasonable length constraints
        response = summarizer(prompt, max_length=60, min_length=20, do_sample=False)

        # Extract the summary text from the first result
        return response[0]['summary_text']
    except Exception as e:
        # Catch and return any error message as a string
        return f"Error in response: {str(e)}"
