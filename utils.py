from re import search

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI, ChatOpenAI
from openai import api_key
from requests_toolbelt.multipart.encoder import total_len
from langchain_community.utilities import WikipediaAPIWrapper
import os
def PPT_answer(pagination,theme,style,assignment,creativity):
    search=WikipediaAPIWrapper(lang="zh")
    search_result=search.run(theme)
    title_template = ChatPromptTemplate.from_messages(
        "human"
        f"""你现在是一位专业的PPT设计师，我需要你详细地帮我规划PPT的标题，PPT的主题是{theme}，风格是{style},标题要求逻辑清晰，适合用于PPT展示"""
    )
    script_template = ChatPromptTemplate.from_messages(
        "human"
        f"""'''{WikipediaAPIWrapper(lang="zh")}'''"""
    )
    final_prompt_template = ChatPromptTemplate.from_messages(
        "human"
        """"""
    )
    model = ChatOpenAI(model="gpt-3.5-turbo",api_key="hJXuWUvSZFW1Yf0Z6nM2UVt1g5t24ru1UldYNyO7pdUMWJ7b",temperature=creativity,base_url="https://api.aigc369.com/v1")
    title_chain = title_template | model
    script_chain = script_template | model
    title = title_chain.invoke({"style":style,"theme":theme}).content
    script = script_chain.invoke({"style":style,"title":title,"pagination":pagination,"assignment":assignment,"creativity":creativity,"Wikipedia_search":search_result}).content
    return title,script,search


