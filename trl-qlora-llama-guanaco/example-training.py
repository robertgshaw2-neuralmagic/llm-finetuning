import os, torch, argparse
from datasets import load_dataset
from peft import LoraConfig, PeftModel
from transformers import AutoModelForCausalLM, Trainer, AutoTokenizer, TrainingArguments

MODEL_ID = "meta-llama/Llama-2-7b-hf"
DTYPE = torch.bfloat16


try:
    HF_TOKEN = os.environ["HF_TOKEN"]
except:
    raise ValueError("Set HF_TOKEN enviornment variable to your access token to run the script")

def run():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.add_special_tokens({"pad_token":"<pad>"})
    tokenizer.padding_side = 'left'

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch_dtype,
    )

    
if __name__ == "__main__":
    run()