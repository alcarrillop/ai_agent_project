from transformers import pipeline

# Quick test to see if transformers library is working
test_pipeline = pipeline("text-generation", model="gpt2", device=0)
response = test_pipeline("Hello, this is a test", max_length=10)
print(response)
