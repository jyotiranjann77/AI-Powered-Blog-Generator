from transformers import pipeline
import gradio as gr

# Function to generate blog
def generate_blog(topic, word_limit=300):
    """Generate a blog with Introduction, Main Body, and Conclusion."""
    text_generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2")

    # Generate blog sections
    introduction = text_generator(f"Write an introduction about {topic}.", max_length=word_limit // 3, num_return_sequences=1)[0]['generated_text']
    main_body = text_generator(f"Discuss in detail about {topic}.", max_length=word_limit // 2, num_return_sequences=1)[0]['generated_text']
    conclusion = text_generator(f"Conclude a blog about {topic}.", max_length=word_limit // 4, num_return_sequences=1)[0]['generated_text']

    # Combine the sections into a single blog
    blog = f"### Introduction\n\n{introduction}\n\n### Main Body\n\n{main_body}\n\n### Conclusion\n\n{conclusion}"
    return blog


if __name__ == "__main__":
    # For local testing
    topic = input("Enter a topic: ")
    word_limit = int(input("Enter word limit (100-600): "))

    blog = generate_blog(topic, word_limit)
    print("\nGenerated Blog:\n")
    print(blog)

   
    interface = gr.Interface(
        fn=generate_blog,
        inputs=[
            gr.Textbox(label="Enter a topic", placeholder="e.g., Artificial Intelligence"),
            gr.Slider(100, 600, value=300, step=50, label="Word Limit")
        ],
        outputs=gr.Markdown(label="Generated Blog"),
        title="AI-Powered Blog Generator",
        description="Enter a topic, and this tool will generate a blog with Introduction, Main Body, and Conclusion."
    )
    interface.launch()
