

# bootstrap

Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery.Currently version is 4.3.1.

## bootstrap最基本的模版

```html
<!doctype html>
<html lang="ch-ZN">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <!--这个是响应式开发、移动优先所必须设置的 -->
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS,是必须设置的 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```

HTML5声明：

```html
<!doctype html>
<html lang="en">
  ...
</html>
```

## bootstrap布局容器container

布局容器是使用默认网格系统时最基本的布局元素，bootstrap提供了2种类型的容器，一种是container，是固定宽度的容器。

```html
<div class="container">
  <!-- Content here -->
</div>
```

另一种是container-fluid，是始终100%宽度的容器。

```html
<div class="container-fluid">
  ...
</div>
```

## bootstrap组件的使用

### 字体图标

在bs4中，默认没有字体图标了，但是可以将其他库引入项目中，官方推荐的方式有：

- [Font Awesome](https://fontawesome.com/)
- [Iconic](https://github.com/iconic/open-iconic)
- [Octicons](https://octicons.github.com/)

这里以font awesome为例，介绍其用法：

首先在head标签中引入js文件，然后就可以在body中使用了。

```html
<script src="https://kit.fontawesome.com/74370c2f86.js"></script>
<!-- 样式需要自己写css，Class后面的名称是根据相应图标的名字-->
<div style="font-size:50px;color:red" class="fas fa-ad"> </div>
```

字体图标可以在div标签、button标签中使用。

### button

默认的button类型有：

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
<button type="button" class="btn btn-link">Link</button>
```

除了用button标签来定义按钮，还可以将a、input标签渲染为button标签，注意的是a标签渲染时要加role属性。

```html
<a class="btn btn-primary" href="#" role="button">Link</a>
<button class="btn btn-primary" type="submit">Button</button>
<input class="btn btn-primary" type="button" value="Input">
<input class="btn btn-primary" type="submit" value="Submit">
<input class="btn btn-primary" type="reset" value="Reset">
```

外边框按钮

如果只需要按钮，不需要它默认的背景色，则可以使用下面的方式：

```html
<button type="button" class="btn btn-outline-primary">Primary</button>
<button type="button" class="btn btn-outline-secondary">Secondary</button>
<button type="button" class="btn btn-outline-success">Success</button>
<button type="button" class="btn btn-outline-danger">Danger</button>
<button type="button" class="btn btn-outline-warning">Warning</button>
<button type="button" class="btn btn-outline-info">Info</button>
<button type="button" class="btn btn-outline-light">Light</button>
<button type="button" class="btn btn-outline-dark">Dark</button>
```

按钮大小设置

在class属性中加入：btn-lg(大图)、btn-sm（小图）即可。

按钮激活状态和禁用状态

在class属性中加入active、disabled。

按钮中加入图标

### 下拉菜单

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown button
  </button>
  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>
```

