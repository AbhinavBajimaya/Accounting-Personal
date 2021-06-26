from django.db import models
import datetime

# Create your models here

#name and description of individual items.
class Item(models.Model):
    item_type = models.CharField(max_length=30)
    model_name = models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    quantity=models.PositiveIntegerField(default=0)
    #total_in_quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField(max_length=100)
    #in_stock=models.BooleanField(default=False)
    is_stock=models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_type + " " + self.model_name

    def set_is_stock(self):
        if self.quantity == 0:
            self.is_stock=False
        else:
            self.is_stock=True
        self.save()
        

#from where items are imported
class Importer(models.Model):
    name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone_number=models.DecimalField(max_digits=10, decimal_places=0)
    vat_number=models.DecimalField(max_digits=15, decimal_places=0)
    pan_number=models.DecimalField(max_digits=15, decimal_places=0)
    def __str__(self):
        return self.name 

#details of customer
class Customer(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone_number=models.DecimalField(max_digits=10, decimal_places=0)
    vat_number=models.DecimalField(max_digits=15, decimal_places=0)
    pan_number=models.DecimalField(max_digits=15, decimal_places=0)
    def __str__(self):
        return self.name

#individual items and quantities on stocking
class stock_item(models.Model):    
    current=models.BooleanField(default=True)
    items=models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField()
    in_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return "(" + str(self.quantity) + ")" + self.items.model_name + " at "  + str(self.in_price) + " = " + str(self.in_price*self.quantity)

    

#total bill transactions and list of items/quantities on stocking
class stock_total(models.Model):
    importer=models.ForeignKey(Importer, on_delete=models.PROTECT)
    items=models.ManyToManyField(stock_item)
    added_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2,default=0)

    def __str__(self):
        return self.importer.name + " " + self.added_at.strftime('%m/%d/%Y')

    def get_total_price(self):
        total = 0
        for item in items:
            total += item.total_price
        return total
    
    
#individual items and quantities on sales
class sale_item(models.Model):
    items=models.ForeignKey(Item,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return self.items.model_name + " " + "(" + str(self.quantity) + ")"


#total sale bill items and quantities    
class sale_total(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True)
    items=models.ManyToManyField(sale_item)  
    sold_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.customer.name + " " + self.sold_at.strftime('%m%d%y')

class account(models.Model):
    name=models.CharField(max_length=40)
    expense_out = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    revenue_in  = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    stock_price  = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    profit = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def get_stock_price(self):
        sum=0
        for item in Item.objects.filter(is_stock=True):
            total=item.quantity*item.price
            sum += total
        self.stock_price=sum
        self.save()
        return sum

    def __str__(self):
        return self.name

    
#in the case of customer returning an item
#class return_item(models.Model):
 #   customer=models.ForeignKey(Customer, on_delete=models.PROTECT)
  #  items=models.ForeignKey(Item, on_delete=models.PROTECT)
   # quantity=models.PositiveIntegerField()
    #returned_at=models.DateTimeField(auto_now_add=True)


    





