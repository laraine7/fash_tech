# encoding: utf-8

import random,time,os
from fash_tech_end.lee_selenium import Lee

class ComfirmOrder(Lee):
    '''定位器'''

    Change_address_loc=("link text","更改")

    Add_new_address_loc=("link text","使用新地址")

    Add_gift_code_loc=("css selector",".left>input")

    Add_gift_button_loc=("css selector",".right>button")

    Payment_method_loc=("css selector",".label-list>label>input")

    Pay_now_loc=("css selector","#sub")

    Payment_succes_loc=("link text","已完成付款")

    Payment_fail_loc=("link text","付款遇到问题")


    #操作方法

    def Payment_method(self):

        self.js_scoll_end()

        number=self.random_randint(self.Payment_method_loc)

        self.clicks(self.Payment_method_loc,number)

    def Pay_now(self):

        self.click(self.Pay_now_loc)

    def Payment_succes(self):
        self.click(self.Payment_succes_loc)
