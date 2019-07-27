# 线性表
## 1、线性表以及基本操作
### 1.1、基本概念
{a0,a1,a2,···ai,ai+1,···,an-1}  
ai可以是字母、整数、浮点数、对象或其他更加复杂的信息  
### 1.2、抽象数据类型描述
```python
from abc import ABCMeta, abstractmethod, abstractproperty
class IList(metaclass=ABCMeta):
    @abstractmethod
    def clear(self):
        pass
    @abstractmethod
    def isEmpty(self):
        pass
    @abstractmethod
    def length(self):
        pass
    @abstractmethod
    def get(self, i):
        pass
    @abstractmethod
    def insert(self, x):
        pass
    @abstractmethod
    def remove(self, i):
        pass
    @abstractmethod
    def index(self, x):
        pass
    @abstractmethod
    def display(self):
        pass
```
### 1.3线性表的存储和实现

(1)、基于顺序表存储的实现  
(2)、基于链式存储的实现  

## 2、线性表的孙顺序存储
### 2.1顺序表
#### 2.1.1、定义
#### 2.1.2、特点
#### 2.1.3、描述
### 2.2顺序表的基本操作实现
## 3、线性表的链式存储和实现
### 3.1单链表
### 3.2单链表的基本操作实现
### 3.3其他链表
## 4、顺序表与链表的比较
