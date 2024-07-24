## Training von Bloomz-1b1 Modell mit LoRA Methode
import torch
import torch.nn as nn
#import bitsandbytes as bnb
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling
import Training.daten_verarbeitung as train_daten

#Modell laden
checkpoint = "bigscience/bloomz-1b1"

model = AutoModelForCausalLM.from_pretrained(
    checkpoint,
    device_map='auto'
)

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# Konfigurationsinformationen von Bloomz-1b1 Modell
config = AutoConfig.from_pretrained(checkpoint)
#print(config)

# Traverse Parameter
#para1 = list(model.parameters())[0].dtype  # torch.float32
for i, param in enumerate(model.parameters()):
    param.requires_grad = False  # Modell einfrieren - Adapter später trainieren
    if param.ndim == 1:
        param.data = param.data.to(torch.float32)

#model.gradient_checkpointing_enable()
#model.enable_input_require_grads()

class CastOutputToFloat(nn.Sequential):
    def forward(self, x):
        return super().forward(x).to(torch.float32)
model.lm_head = CastOutputToFloat(model.lm_head)

# Druckt die Anzahl der trainierbaren Parameter im Modell.
def print_trainable_parameters(model):
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
    )

# Konfigurieren Lora-Parameter
config = LoraConfig(
    r=16,
    lora_alpha=32,
    # target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model_peft = get_peft_model(model, config)
print_trainable_parameters(model_peft)
#print(model_peft)

# Datensatz laden
dataset = train_daten.data_vorverarbeitung()

# Konfigurieren Training-Parameter
trainer = Trainer(
    model=model_peft,
    train_dataset=dataset['train'],
    args=TrainingArguments(
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=100,
        max_steps=2000,
        learning_rate=3e-5,
        #fp16=True,
        logging_steps=1,
        logging_dir='E:/BA/Output_LLM/Bloomz_1b1_lora',
        output_dir='E:/BA/Output_LLM/Bloomz_1b1_lora'
    ),
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
)
model_peft.config.use_cache = False
trainer.train()

# Spreichen Modell
model_id_lora = "E:/BA/Output_LLM/Bloomz_1b1_lora/model"
model_peft.save_pretrained(model_id_lora)


