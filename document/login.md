# 用户登录

post参数只需包含**name**和**pwd**，不做参数正确性验证，执行成功可查看到cookie中的token值，并返回成功信息

```
 post {{url}}/login
  -data '{"name": "dudu", "pwd": "1111"}'
```

返回结果：
```
成功：
{ "message": "登录成功" }
失败：
{ "error": "请求参数错误" }
```

# 获取登录信息
```
 get {{url}}/login
```
返回结果：
```
成功：
{ "name": "dudu" }
失败：
{ "error": "token错误" }
```

### 待完成
> cookie_update 中更新最近浏览记录 p25
> clean_session 定时检查token数量，移除旧令牌 p26