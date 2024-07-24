# Verarbeitung von Datensatz für Training
from datasets import load_dataset
from transformers import AutoTokenizer

def data_vorverarbeitung():
    checkpoint = "bigscience/bloomz-1b1"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    # Datensätze laden
    data_files = {"train": "E:/BA/Datenset/LLMs_training/train.json", "test": "E:/BA/Datenset/LLMs_training/dev.json"}
    dataset = load_dataset("json", data_files=data_files)

    # Neuformatierung
    def create_prompt(question, answer):
        prompt_template = f"QUESTION:\n{question}\n\nANSWER:\n{answer}</s>"
        return prompt_template

    # Anwenden der Neuformatierungsfunktion auf den gesamten Datensatz
    mapped_dataset = dataset.map(lambda samples: tokenizer(create_prompt(samples['Question'], samples['Answer'])))
    #dataset_pandas = mapped_dataset['train'].to_pandas()
    return mapped_dataset

data_vorverarbeitung()

