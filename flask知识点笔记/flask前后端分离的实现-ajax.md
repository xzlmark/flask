# flask中前后端分离

视图中可以返回response、json、abort、redirect等，一般数据传输用json.

view中实现如下：

```python
@blue.route('/score/')  # 前后端分析，通过json数据传递给前端静态网页，存在于static文件夹中
def get_score():
    score = {
        'data':[50,30,60,88,90]
    }
    return jsonify(score)
```

在纯静态网页中，位于static文件夹下score.html

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>得分榜-前后端分离</title>
    <script src="http://code.jquery.com/jquery-3.4.1.min.js"></script>  这个是从http://code.jquery.com/中获取的接口
    <script type="text/javascript">
        $(function () {
            $.getJSON("/score/", function (data) {
                console.log(data)；
                var scores = data["data"];
                var $ul = $("#score_container");
                for (var i = 0; i
                < scores.length; i++) {
                    var $li = $("<li></li>").html(scores[i]);
                    $ul.append($li);
                }
            })
        })
	</script>
</head>
<body>
<h1>flask中的前后端分离的实现，用ajax实现</h1>
<ul id="score_container">

</ul>
</body>
</html>
```

这时，浏览器请求的地址就不再是views中的地址，而是静态地址：<http://127.0.0.1:5000/static/score.html>

