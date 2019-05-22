from shopping_car_app.models import TBook


class Book:
    def __init__(self, book, amount):
        self.book = book  # 书的对象
        self.amount = amount  # 本数
        self.per_total_price=0
        self.per_mark_price=0
        self.save_price=0

class Car:
    def __init__(self):
        self.total_price = 0
        self.list1 = []
        self.list2 = []
        self.mark=0
    def sums(self):
        # 计算及其总价
        self.total_price=0
        self.mark=0
        for i in self.list1:
            i.per_total_price = i.book.dangdang_price * i.amount
            self.total_price += i.book.dangdang_price * i.amount
            i.per_save_price=(i.book.mark_price-i.book.dangdang_price)*i.amount
            self.mark+=(i.book.mark_price-i.book.dangdang_price)*i.amount
    def add_mark(self, bookid,amount):
          # 添加购物车
        for i in self.list1:
            if i.book.id == int(bookid):
                i.amount += amount
                self.sums()
                return

        book = TBook.objects.get(id=bookid)
        self.list1.append(Book(book, amount))
        self.sums()
    def change_car(self, bookid, amount):  # 修改购物车,改变商品数量，出入一个新的amount进行改变
        for i in self.list1:
            if i.book.id == bookid:
                i.amount = amount
                self.sums()  # 总价也会改变
                return

    def del_car(self, bookid):  # 删除购物车，找到对应id的产品删除
        for i in self.list1:

            if i.book.id == int(bookid):
                self.list2.append(i)
                self.list1.remove(i)

        print(self.list2,self.list1)
        self.sums()

    def huifu_car(self,bookid,amount):
        print(self.list2)
        for i in self.list2:
            print(bookid,i.book.id)
            if i.book.id==bookid:
                print(self.list1, self.list2)
                self.list2.remove(i)
                self.list1.append(i)
        self.sums()