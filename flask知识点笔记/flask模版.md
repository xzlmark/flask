# flask模版

模版是呈现给用户的界面

模版处理分为两个过程：加载、渲染

模版代码包含两个部分：静态HTML、动态插入的代码段

模版语法主要分为两种：变量、标签

模版中的变量{{ var}} :视图传递给模版的数据，前面定义出来的数据，变量不存在，默认忽略。

模版中的标签：{%tag%}:控制逻辑，使用外部表达式，创建变量，宏定义等

结构标签：block

​	{% block XXX%}

​	{%endblock %}

块操作，覆膜板挖坑，子模版填坑。

extends

{%extends xxx%}  继承后保留块中的内容

挖坑继承体现的是化整为零的操作。 

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    {%block extcss %}
    {% endblock %}
</head>
<body>
{%block header %}
{% endblock %}

{%block content %}
{% endblock %}

{%block footer %}
{% endblock %}

</body>
</html>
```

index.html

```html
{%extends 'base.html'%}
{% block header%}
<h1>这就是继承，模版语言</h1>
{% endblock %}
```

