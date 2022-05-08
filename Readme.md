# 疯狂出题器
By : Biang
## 介绍

基于python开发的一个纯代码没有GUI的究极轻量级刷题notebook(需要自己准备docx文件)

## 需要安装的库

```powershell
pip install python-docx
```

## 题目识别格式
当 

```python
separator_between_number_and_question_text = '.'
separator_between_option_and_option_text = ','
separator_between_answer_tag_and_answer = ':'
```

时，格式如下

```
number1.question_text

option1,option1_text

option2,option2_text

...

optionN,optionN_text

answer_tag: answer


number2.question_text

option1,option1_text

option2,option2_text

...

optionN,optionN_text

answer_tag: answer

...
```

## 配置信息相关

```python
file_path = "xxx.docx" 									#文件名

question_type = {
    "single":False,
    "multiple":True,
    "T_or_F":False
}														 #题型 单选、多选、判断
separator_between_number_and_question_text = '、'		#题号和问题之间的分隔符
separator_between_option_and_option_text = '、'			#选项和选项内容之间的分隔符
separator_between_answer_tag_and_answer = '：'			#答案标签和答案之间的分隔符
answer_tag = '答案'										#答案标签
T_or_F_options = ['正确','错误']						  #判断题的选项文字
```

## 使用方法

以pycharm为例,将前面配置信息、导入库、准备工作运行完后，

点击 ```question=Get_question(questions=questions,disposable=True)``` 左边的绿色箭头出题目

点击 ```Get_answer(answer_tag=answer_tag,question=question)``` 左边的绿色箭头出答案

![example](https://raw.githubusercontent.com/BIANG-qilie/Crazy-Question-Maker/master/image/example.png)

其中 disposable=True时不会做到重复的题目，反之则会

