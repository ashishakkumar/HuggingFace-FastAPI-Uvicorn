### FASTAPI EXAMPLE FOR DEPLOYING MODEL PULLED FROM HUGGINGFACE
<div align="center">
<img src="https://www.bing.com/images/create/huggingface-and-fastapi-in-the-same-image/1-65f72064ce8b472fa48ac46232fe6ae5?id=CnUoRTXFRDEmFA4uGkYH2w%3d%3d&view=detailv2&idpp=genimg&thId=OIG3.p39IuQA.LirrvwSOnSn_&FORM=GCRIDP&mode=overlay" alt="My Image" width="400" height="400">
</div>

- Hosted gemma 2b-it (without bitsandbytes config) : can uncomment line <  quantization_config=bnb_config, > to load the quantized model
- POST accepts any Research Paper's abstract as input and try to reporduce the title that maximises the clickbait as output
- The gemma 2b-it model is loaded with a PeftAdapter derived from QLoRA fine tuning the gemma 2b-it model on dataset [https://huggingface.co/datasets/ashishkgpian/astromistral] containing the abstract and title of different scientific/research papers shown to have maximum reads, even without having citations [clickbait possibility]
