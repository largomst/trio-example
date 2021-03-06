# Python 异步编程

该项目是在学习使用 Python 的 asyncio 和 trio 的一些示例代码。

## 第一个示例

按照 trio 官方文档的说法，一个典型的 Python 的异步程序是三明治结构的：

trio.run -> [async function] -> ... -> [async function] -> trio.whaterver

async 函数被包含在 trio.run 和 trio.whatever 中。

## 第二个示例

在 trio 中我们通过 nursery 来启动多个子 async 函数，最终还是由 trio.run 来启动作为 parent 的 async 函数。

这里值得注意的是 nursery 是通过异步上下文管理器来创建的，异步上下文管理器和上下文管理器的区别在于其 __enter__ 和 __exit__ 方法变成了异步的 __aenter__ 和 __aexit__，保证了 parent 也是 async 函数。

## 第三个示例

要如何获得异步函数的返回值呢？异步和多线程在很多地方是相似的，例如子线程和父线程之间的通讯通常通过 Queue 来实现。

在异步编程中，我们仍然可以使用 Queue 来实现同样的操作。

## 第四个示例

怎么让那些可能造成阻塞的同步函数变成异步函数呢？答案是使用 trio.to_thread.run_sync，可以将同步函数放到一个线程中去执行，从而达到异步的效果。

## 第五个示例

#TODO

## 第六个示例

和 golang 自带的 channel 一样，trio 中的 channel 可以用来实现通信。

通道可以设置缓冲大小，如果是 0，表示无缓冲，发送方会在发送后一直阻塞，直到接收方接收到数据。而接收方则会在接收到数据前一直阻塞，直到接受到数据。

当缓冲区大小不为 0 时，只有当发送方发送的数据大于缓冲区大小时，才会引发阻塞。

基于通道的通信，可以很容易地实现生产者消费者模式。

