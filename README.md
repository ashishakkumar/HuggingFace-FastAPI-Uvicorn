- Hosted gemma 2b-it (without bitsandbytes config) : can uncomment line <  quantization_config=bnb_config, > to load the quantized model
- POST accepts any Research Paper's abstract as input and try to reporduce the title that maximises the clickbait as output
- The gemma 2b-it model is loaded with a PeftAdapter derived from QLoRA fine tuning the gemma 2b-it model on dataset [https://huggingface.co/datasets/ashishkgpian/astromistral] containing the abstract and title of different scientific/research papers shown to have maximum reads, even without having citations [clickbait possibility]
