from typing import Any
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import tensorflow as tf
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
from peft import PeftModel, PeftConfig


bnb_config = BitsAndBytesConfig(  
    load_in_4bit= True,
    bnb_4bit_quant_type= "nf4",
    bnb_4bit_compute_dtype= torch.bfloat16,
    bnb_4bit_use_double_quant= False,
)


# GGML model required to fit Llama2-13B on a T4 GPU

GENERATIVE_AI_MODEL_REPO = "google/gemma-2b-it"
GENERATIVE_AI_MODEL_ADAPTER = "ashishkgpian/gemma_unsloth"

from transformers import pipeline, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained(
        'google/gemma-2b-it',

        # quantization_config=bnb_config,

        device_map="auto",
    
    
        trust_remote_code=True,)


tokenizer = AutoTokenizer.from_pretrained(GENERATIVE_AI_MODEL_REPO, trust_remote_code=True)
model = PeftModel.from_pretrained(model, GENERATIVE_AI_MODEL_ADAPTER)



def formatting_func(example):
    text = f"### Instruction :{example['instruction']}\n\n### Input:{example['input']}\n\n### Response : "
    return text



from datetime import datetime
from transformers import pipeline
import re

def model_seq_gen(abstract, model= model,temp = 0.5) : 
        example = {'instruction' : 'Write a catchy title for the following paper abstract. The title should be a single sentence that accurately captures what you have done and sounds interesting to the people who work on the same or a similar topic. The title should contain the important title keywords that other researchers use when looking for literature in databases. The title should also use synonyms, broader terms, or abstractive keywords to make it more appealing and informative. Do not use words that are not related to the paper extract or the topic',
    'input' : abstract }
        eval_prompt = formatting_func(example)
        pipe = pipeline(task="text2text-generation", model=model, tokenizer=tokenizer)
        start = datetime.now()
        sequences = pipe(
            f'{eval_prompt}' ,
            do_sample=True,
            max_new_tokens=50, 
            temperature=temp, 
            top_k=50, 
            top_p=0.95,
            num_return_sequences=1)
        
        try : 
            extracted_title = re.sub(r'[\'"]', '', sequences[0]['generated_text'].split("Response : ")[1])
        except :
            extracted_title = sequences[0]['generated_text'] 
            
        stop = datetime.now()
        time_taken = stop-start
        print(f"Execution Time : {time_taken}")
        return extracted_title


app = FastAPI()

# This defines the data json format expected for the endpoint, change as needed
class TextInput(BaseModel):
    inputs: str
    parameters: dict[str, Any] | None

@app.get("/")
def status_gpu_check() -> dict[str, str]:
    gpu_msg = "Available" if tf.test.is_gpu_available() else "Unavailable"
    return {
        "status": "I am ALIVE!",
        "gpu": gpu_msg
    }

@app.post("/generate/")
async def generate_text(data: TextInput) -> dict[str, str]:
    try:
        print(type(data))
        print(data)
        params = data.parameters or {}
        response = model_seq_gen(abstract=data.inputs, **params)
        
        return {"generated_text": response}
    except Exception as e:
        print(type(data))
        print(data)
        print(e)
        raise HTTPException(status_code=500, detail=len(str(e)))
    

# The server will start the model download and will take a while to start up
# ~5 minutes if its not already downloaded

