# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BookKind(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'book_kind'


class TAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 't_address'


class TBook(models.Model):
    book_name = models.CharField(max_length=100, blank=True, null=True)
    book_kind = models.ForeignKey(BookKind, models.DO_NOTHING, db_column='book_kind', blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    publish = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    print_times = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    word_num = models.CharField(max_length=100, blank=True, null=True)
    page_num = models.CharField(max_length=100, blank=True, null=True)
    page_size = models.CharField(max_length=100, blank=True, null=True)
    paper = models.CharField(max_length=100, blank=True, null=True)
    packing = models.CharField(max_length=100, blank=True, null=True)
    mark_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    dangdang_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    series_name = models.CharField(max_length=100, blank=True, null=True)
    editor_recommendation = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    introduce_author = models.CharField(max_length=100, blank=True, null=True)
    media = models.CharField(max_length=100, blank=True, null=True)
    pic_book = models.CharField(max_length=100, blank=True, null=True)
    ground_time = models.DateTimeField(blank=True, null=True)
    off_time = models.DateTimeField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    sales_volume = models.IntegerField(blank=True, null=True)
    recommend = models.IntegerField(blank=True, null=True)
    cus_score = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:

        db_table = 't_book'


class TOrder(models.Model):
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    book_count = models.IntegerField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    finish = models.IntegerField(blank=True, null=True)
    finish_times = models.IntegerField(blank=True, null=True)
    id = models.ForeignKey(TBook, models.DO_NOTHING, db_column='id', primary_key=True)
    addrees = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)

    class Meta:

        db_table = 't_order'


class TUser(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    sale = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 't_user'
