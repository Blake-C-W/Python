class employee:
    def revenue_generated(self,x,y):
        return x * y


employee_1 = employee()
employee_1.name = 'Employee 1'
employee_1.id = 'ID123456789'
employee_1.email = 'employee1@company_name.com'
employee_1.number_of_sales = 50
employee_1.sale_price = 10

print(employee)
print(employee_1.name)
print(employee_1.id)
print(employee_1.email)
print(employee_1.revenue_generated(employee_1.number_of_sales,employee_1.sale_price))
