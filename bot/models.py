import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from config import MODEL_NAME


# Убедитесь, что используется CPU
device = torch.device("cpu")

# Загрузка модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt: str, max_length: int, temperature: float) -> str:
    """
    Генерация ответа с помощью модели.
    """
    response = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=1,
        truncation=True,
        do_sample=True 
    )
    return response[0]['generated_text']