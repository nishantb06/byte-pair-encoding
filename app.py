import gradio as gr
from minbpe.regex import RegexTokenizer
from typing import List, Dict

# Initialize the tokenizer
tokenizer = RegexTokenizer()
tokenizer.load("modelsV3-regex-new-testament-only/regex.model")


def process_text(text: str) -> str:
    # Get token IDs
    token_ids = tokenizer.encode(text)

    # Build formatted output
    output = []
    output.append("Token Details:")
    output.append("-" * 50)

    for token_id in token_ids:
        # Get the bytes for this token
        token_bytes = tokenizer.vocab[token_id]
        # Convert bytes to string representation, replacing invalid chars
        token_text = token_bytes.decode("utf-8", errors="replace")

        output.append(f"Token ID: {token_id}")
        output.append(f"Token Bytes: {str(token_bytes)}")
        output.append(f"Token Text: {token_text}")
        output.append("-" * 50)

    # Add decoded text at the end
    decoded_text = tokenizer.decode(token_ids)
    output.append(f"\nFull decoded text: {decoded_text}")

    return "\n".join(output)


# Create Gradio interface
demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter text to tokenize", lines=3),
    outputs=gr.Textbox(label="Token Information", lines=10),
    title="Hindi Text Tokenizer",
    description="Enter Hindi text to see its token representation using Byte Pair Encoding",
    examples=[["उज्जियाह से योताम उत्पन्न"], ["नमस्ते दुनिया"]],
)

if __name__ == "__main__":
    demo.launch()
