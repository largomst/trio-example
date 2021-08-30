# Python 异步编程

该项目是在学习使用 Python 的 asyncio 和 trio 的一些示例代码。

## 第一个示例

按照 trio 官方文档的说法，一个典型的 Python 的异步程序是三明治结构的：

trio.run -> [async function] -> ... -> [async function] -> trio.whaterver

async 函数被包含在 trio.run 和 trio.whatever 中。

