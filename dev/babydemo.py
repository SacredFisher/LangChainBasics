import os

os.environ['OPENAI_API_KEY'] = ''
os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
#Get these

#_____________________OpenAI

from langchain.llms import OpenAI

llm  = OpenAI( model_name = 'text-davinci-003',
               temperature = .09,
               max_tokens = 256)

text = "reverse this phrase: hello"

print('Model: text-davinci-003')
print(f'Text: { text }')
print(f'Response: { llm(text) }')


