import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain import OpenAI, ConversationChain


os.environ["OPENAI_API_KEY"] = "..."



llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))




prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)


print(prompt.format(product="colorful socks"))




llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)



chain = LLMChain(llm=llm, prompt=prompt)


chain.run("colorful socks")


llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")
print(output)


output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)
