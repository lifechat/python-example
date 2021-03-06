
# XPath 语法



**下面是一个基本语法元素的列表，你将用它来组合你的XPath表达式。**

- **节点:**  有不同类型的节点，根节点、元素节点、属性节点，以及所谓的原子值，这是HTML文档中文本节点的同义词。

- **父元素:** 包含当前元素的直接元素。每个元素节点都有一个父节点。在我们上面的例子中，html是head和body的父元素，而body是网站实际内容的父元素。

- **子元素:** 当前元素所包含的直接元素。元素结点可以有任何数量的子元素。在我们的例子中，h1和两个p元素都是body的子女。

- **同代元素:** 与当前元素处于同一级别的节点。在我们的例子中，head和body是兄弟姐妹（在它们作为html的子女的功能中），h1和两个p元素也是兄弟姐妹（在它们作为body的子女的功能中）


**下面是一个基本语法元素的列表，你将用它来组合你的XPath表达式。**


|    XPath元素     |                   描述信息                    |
|:--------------:|:-----------------------------------------:|
|      节点名字      |           这是最简单的一个,它选择所有节点与节点名            |
|       /        |              选择从根节点(用于绝对路径)               |
|       //       |           从当前节点选中符合条件的node节点和元素           |
|       .        |                  选择当前节点                   |
|       ..       |                选择当前节点的父元素                 |
|       @        |               选择符合属性的元素和节点                |
|       *        |                  匹配任意元素                   |
|  preceding::   |               查找当前节点之前的所有节点               |
|  following::   |               查找当前节点之后的所有节点               |
| function() 函数体 | 给定的上下文进行调用xpath库自带的函数，例如text(),contains() |



