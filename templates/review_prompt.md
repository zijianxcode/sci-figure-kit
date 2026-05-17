# Figure Review Prompt

请按学术论文配图标准审查这张图。

## 图的任务

{task_sentence}

## 正文依据

```text
{source_context}
```

## 图注

```text
{caption}
```

## 审查维度

1. Faithfulness  
   图中元素是否都能在正文中找到依据？是否引入了正文没有支撑的概念？是否扭曲了概念层级？

2. Conciseness  
   图是否只是正文的盒子化搬运？是否存在可以删掉的解释句、图例、重复信息？

3. Readability  
   A4 宽度下能否读清？布局是否紧凑？图题和图片是否可能分页分离？

4. Aesthetics  
   色彩是否服务于结构？线型是否有语义？是否有过度装饰？

## 输出格式

```text
主要问题：
- 

建议修改：
- 

是否适合进入论文正文：是 / 否 / 修改后可用
```

