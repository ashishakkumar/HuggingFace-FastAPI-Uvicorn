# FastAPI for deploying model pulled from HuggingFace
<div align="center">
<img src="https://github.com/ashishakkumar/HuggingFace_FastAPI/blob/main/OIG3.p39IuQA.jpeg" alt="My Image" width="400" height="400">
</div>

- Hosted gemma 2b-it (without bitsandbytes config) : can uncomment line <  quantization_config=bnb_config, > to load the quantized model
- POST accepts any Research Paper's abstract as input and try to reporduce the title that maximises the clickbait as output
- The gemma 2b-it model is loaded with a PeftAdapter derived from QLoRA fine tuning the gemma 2b-it model on dataset [https://huggingface.co/datasets/ashishkgpian/astromistral] containing the abstract and title of different scientific/research papers shown to have maximum reads, even without having citations [clickbait possibility]

To run it locally : 
1. Clone the repository
```python
git clone https://github.com/ashishakkumar/HuggingFace-FastAPI-Uvicorn.git
``````
2. Create a virtual environment in the directory
```python
>> python -m venv virtual_environment_name
``````
3. Activate the environment
```python
>> source virtual_environment_name/bin/activate
``````
4. Install all the required libraries
```python
>> pip install -r requirements.txt
``````
5. Setup the server 
```python
>> uvicorn main:app --reload
``````
After the server is setup for running the api, you can check more about the inputs and outputs by running ```http://127.0.0.1:8000/docs``` in the browser
