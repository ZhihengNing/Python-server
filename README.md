# Python服务脚手架

用于将工程算法以简单无脑的方式接入到python服务中，并支持通过API的形式访问

## 要求

python版本大于等于3.10

## 运行

运行requirements.txt

```python
pip install -r requirements.txt
```

打开algorithm.py，将工程算法中的参数和方法体依次放入implement方法的参数和方法体中，下面是一个算法示意代码

```python
class Algorithm(BaseAlgorithm):
    def implement(self, a, b):
        return {
            'a': np.array([1, 3]),
            'b': {
                "2": {1, 2, 3},
                "c": a / sum(b.c)
            }
        }
```

运行main.py文件

```
python main.py
```

通过postman发送Post请求，URL为http://localhost:5000/analyse

![image-20240613213435081](README.assets/image-20240613213435081.png)

