from re import search

import streamlit
from utils import PPT_answer

streamlit.title("PPT草稿生成器DEMO(●'◡'●)")
pagination=streamlit.text_input("请输入PPT的页数🤞")
style=streamlit.text_input("请输入PPT的制作风格😘")
assignment=streamlit.text_input("请输入PPT的目标任务😎")
theme=streamlit.text_input("请输入PPT的主题😉")
creativity=streamlit.slider("请选择PPT的创造性🤩",min_value=0.0, max_value=2.0,value=0.2,step=0.1)
agree=streamlit.checkbox("本网站为计算机练习生颜子壹练手作，功能不完善，如果PPT被批判，与沃无瓜🧐")
submit=streamlit.button("点击生成")
if submit and  agree:
    with streamlit.spinner("别吵，AI在思考"):
        title,script=PPT_answer(pagination,style,theme,assignment,creativity)
    streamlit.success("已完成！")
    streamlit.write(title)
    streamlit.subheader("草稿")
    streamlit.write(script)
    streamlit.subheader("维基百科参考")
    streamlit.write(search)

























