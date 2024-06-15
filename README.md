### Part#1 银行应用设计
#### a) 需求分析

*1.实体设计*
1. 员工：员工号（PK）、姓名、性别、手机号、工资、等级。
2. 部门：部门号（PK）、部门名称。
3. 银行：银行编号（PK）、银行名称、总资产。
4. 客户：客户号（PK）、姓名、手机号、住址。
5. 账户：账户号（PK）、密码、余额。
6. 贷款：贷款号（PK）、本金、利率、借贷时间。
7. 存款：存款号（PK）、本金、利率、存贷时间。


*2.关系设计*

1. 隶属关系：一个部门有多个员工，但一名员工只能在一个部门，为一对多联系。
2. 包含关系：一个银行包含多个部门，一个部门只属于一个银行，为一对多联系。
3. 雇佣关系：一个银行可以雇佣多个员工，但一名员工只能被一个支行雇佣，为一对多联系。
4. 开户关系：一个银行可以开通多个账户，但一个账户只能由一个银行开通，为一对多关系
5. 拥有关系：一名客户可以拥有多个账户，但一个账户只有一个主人，为一对多联系。
6. 贷款关系：一个账号可能有多个贷款，为一对多关系。
7. 存款关系：一个账号可能有多个存款，为一对多关系。

#### b) ER图
![[Pasted image 20240615144937.png]]

#### c) 模式设计
- 满足3-CNF，即不存在没主属性对于码的局部依赖和传递依赖


### Part#2 实现说明

#### a) 框架

- 使用基于 python 的 Django 框架完成应用的全栈设计与实现 ==>[Django文档](https://docs.djangoproject.com/zh-hans/4.2/contents/)
- 后端数据库使用 mysql_workbench

#### b) UI设计

*1.视图设计*

1. **Forms**：
   - 用于输入密码的简单表单。

2. **AccountPasswordView**（视图）：
   - 使用 `PasswordForm` 对账户（`Account` 模型实例）进行身份验证。
   - 渲染 `account_password.html` 模板。
   - 在密码验证成功后重定向到账户详情页面（`account_detail.html`）。

3. **Home View** (`home` 函数)：
   - 渲染 `home.html` 模板。

4. **Customer Views**：
   - **CustomerListView**, **CustomerDetailView**, **CustomerCreateView**, **CustomerUpdateView**, **CustomerDeleteView**：
     - 处理 `Customer` 模型的增删改查操作。
     - 使用 `CustomerForm` 用于创建和更新操作。

5. **Staff Views**：
   - **StaffListView**, **StaffDetailView**, **StaffCreateView**, **StaffUpdateView**, **StaffDeleteView**：
     - 处理 `Staff` 模型的增删改查操作。
     - 使用 `StaffForm` 用于创建和更新操作。

6. **Account Views**：
   - **AccountListView**, **AccountDetailView**, **AccountCreateView**, **AccountUpdateView**, **AccountDeleteView**：
     - 处理 `Account` 模型的增删改查操作。
     - 使用 `AccountForm` 用于创建和更新操作。
     - **AccountDetailView** 还会获取相关的 `Deposit` 和 `Loan` 记录。

7. **Deposit Views**：
   - **DepositListView**, **DepositDetailView**, **DepositCreateView**, **DepositUpdateView**, **DepositDeleteView**：
     - 处理 `Deposit` 模型的增删改查操作。
     - 使用 `DepositForm` 用于创建和更新操作。
     - **DepositListView** 根据 `account_id` 查询参数过滤存款记录。

8. **Loan Views**：
   - **LoanListView**, **LoanDetailView**, **LoanCreateView**, **LoanUpdateView**, **LoanDeleteView**：
     - 处理 `Loan` 模型的增删改查操作。
     - 使用 `LoanForm` 用于创建和更新操作。
9. **htmls**:
   - 每个视图对应的html文件，在base.html框架下简单改写即可，实现较为简单，在此不一一展示。
10. **calculate_interest**:
   - 在视图文件中实现根据利率和本金计算利息的函数
   - 调用对应的html文件显示出来
   



*2.视图路由*
- 配置URLconf文件，将视图和urls配对，同时加上图片管理文件对应的路径
```js

app_name = 'bank_sys'
urlpatterns = [
    path('', views.home, name='home'),
    path('calculate_interest/', views.calculate_interest, name='calculate_interest'),
    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    # Staff URLs
    ......
    # Account URLs
    ......
    # Deposit URLs
	......
    # Loan URLs
	......
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



#### c) 后端实现

*1.数据库的构建*

- 在django中创建模型，并执行迁移（通过运行 `makemigrations` 命令，Django 会检测你对模型文件的修改，并且把修改的部分储存为一次 _迁移_ ）==>[具体示例](https://docs.djangoproject.com/zh-hans/4.2/intro/tutorial02/)
- 然后使用命令是 migrate，django 的一个自动执行数据库迁移并同步管理你的数据库结构的命令
- 模型文件与mysql中创建表的代码极其相似（因为在做同一件事，django也会自动将模型文件映射成对应的sql中创建表文件）
- model.py 大致如下：
```js
class Customer(models.Model):
    # customer_id = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=50
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    def __str__(self):
        return self.name
```

*2.访问数据库中的数据*
- 使用django中访问数据库的API即可
- 大致示例如下：
```js
>>> from polls.models import Customer
>>> Customer.objects.all()
<QuerySet [<Customer: 张三>, <Customer: 李四>]>
>>> Customer.objects.filter(id=1)
<QuerySet [<Customer: 张三>]>
```

*3.设计触发器*
- 实现当创建一个新账户时，自动给该账户创建一个存款为0的存款
```js
use bank2;
DELIMITER //
CREATE TRIGGER after_account_insert
AFTER INSERT ON bank_sys_account
FOR EACH ROW
BEGIN
    INSERT INTO bank_sys_deposit (principal, interest_rate, deposit_date, account_id)
    VALUES (0, 0, NOW(), NEW.id);
END;
//
DELIMITER ;
```
### Part#3 功能测试

#### a) 截图展示
图片太大 qaq

#### b) 仓库地址
- [链接](https://github.com/fishcsc/USTC-Database)




