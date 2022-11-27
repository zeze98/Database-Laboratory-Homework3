import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='dgu1234!', host='127.0.0.1', database='baemin')


def order_product():
    cursor = cnx.cursor()
    product = ("SELECT * FROM product")
    cursor.execute(product)
    print('-----------------------------------------------')
    print("주문 가능한 음식 리스트 입니다")
    print("메뉴를 보시고 주문을 원하시는 제품의 번호를 입력해주세요")
    print('-----------------------------------------------')

    for food in cursor:
        print(str(food[0]) + '번' + ' 제품명: ' + food[1] + ' 제품설명: ' + food[2] + ' 제품가격: ' + str(food[3]) + '원')

    print('-----------------------------------------------')
    print('주문제품 번호')
    proN = int(input())
    print('주문수량')
    proQ = int(input())
    print(str(proN) + '번 음식 ' + str(proQ) + '개 ' + '주문하시려는게 맞나요?')
    print('맞으시면 1번을 틀리시다면 2번을 입력해주세요')
    TF = int(input())
    if TF == 1:
        print('감사합니다 주문 받은 음식점에서 정성을다해 조리해서 최대한 빠르게 배달해드리겠습니다:)')
        main()
        print()

    elif TF == 2:
        order_product()

    else:
        print('잘못입력하신거 같습니다 다시입력해주세요')
        TF = int(input())

    cursor.close()


def main():
    print()
    print('Database Laboratory Homework 3')
    print('문제번호를 입력해 주세요')
    print("1. Select four queries from the SQL queries in HW2")
    print('2. Implement the following')
    print('3. 주문하기')
    print('4. end')
    PN = int(input())
    if PN == 1:
        print()
        show_four_queries()
    elif PN == 2:
        print('2.1) Define a procedure which contains an aggregate function 시작은 1번을')
        print('2.2) Define a function which returns a value 시작은 2번을')
        print('종료를 원하시면 3번')
        print('을 눌러주세요')
        PN2 = int(input())
        if PN2 == 1:
            print()
            aggreF()
        elif PN2 == 2:
            print()
            return_value_F()
        elif PN2 == 3:
            main()
        else:
            print('잘못입력하신거 같습니다 다시입력해주세요')
            main()
    elif PN == 3:
        order_product()
    elif PN == 4:
        print('Database Laboratory Homework 3 is end')
        print('Thank you')
    else:
        print('잘못입력하신거 같습니다 다시입력해주세요')
        main()


def show_four_queries():
    print()
    print('First: use WHERE')
    cursor = cnx.cursor()
    Uwhere = ("select Consumer_Name, Phone_Number from Consumer where Consumer_Name = 'JaeWoo'")
    print('SQL command: ' + Uwhere)
    cursor.execute(Uwhere)
    print('<--------------------Result-------------------->')
    print('Consumer_Name Phone_Number')
    for name in cursor:
        print(name[0] + '\t\t  ' + str(name[1]))
    print('________________________________________________')
    cursor.close()
    print()
    print('Second: more than one tables in FROM')
    cursor = cnx.cursor()
    Ufrom = ("select * from Restaurant natural join Product")
    print('SQL command: ' + Ufrom)
    cursor.execute(Ufrom)
    print('<--------------------Result-------------------->')
    print(
        'Store_Number, Star_Rating, Store_Telephone_Number, Address, Delivery_Fee, Account_Number, Product_Number, Product_Description, Product_Price')
    for NJ in cursor:
        print(NJ)
    cursor.close()
    print('________________________________________________')
    print()
    print('Third: use SET operation')
    cursor = cnx.cursor()
    Uset = ("(select Product_Name, Product_Price from Product) "
            "union"
            "(select Product_name, Total_Delivery_Amount from Orders)")
    print('SQL commend: ' + Uset)
    cursor.execute(Uset)
    print('<--------------------Result-------------------->')
    print('Product_Name Product_Price')
    for UN in cursor:
        print(UN[0], UN[1])
    cursor.close()
    print('________________________________________________')
    print()
    print('Fourth: use aggregate function and/or GROUP BY')
    cursor = cnx.cursor()
    Uaggre = ("select Order_Number, Total_Delivery_Amount, Product_name from Orders"
              " where Total_Delivery_Amount = (select max(Total_Delivery_Amount) from Orders)"
              " or Total_Delivery_Amount = (select min(Total_Delivery_Amount) from Orders)")
    print('SQL command: ' + Uaggre)
    cursor.execute(Uaggre)
    print('<--------------------Result-------------------->')
    print('Order_Number, Total_Delivery_Amount, Product_Name')
    for UA in cursor:
        print(UA)
    cursor.close()
    print('________________________________________________')
    main()


def aggreF():
    print()
    print('2.1) Define a procedure which contains an aggregate function')
    print('1. 별점이 제일 높은 가게 리스트 보기')
    print('2. 별전이 제일 낮은 가게 리스트 보기')
    print('3. 가장 비싼 음식 리스트 보기')
    print('4. 가장 싼 음식 리스트 보기')
    print('5. 종료')
    n = int(input())
    if n == 1:
        cursor = cnx.cursor()
        starH = ("select Account_Name, Star_Rating"
                 " from Restaurant "
                 "where Star_Rating = (select max(Star_Rating) from Restaurant)")
        cursor.execute(starH)
        for SH in cursor:
            print('가게명: ' + SH[0] + ' 별점: ' + str(SH[1]) + '점')

        aggreF()
    elif n == 2:
        cursor = cnx.cursor()
        starL = ("select Account_Name, Star_Rating"
                 " from Restaurant "
                 "where Star_Rating = (select min(Star_Rating) from Restaurant)")
        cursor.execute(starL)
        for SL in cursor:
            print('가게명: ' + SL[0] + ' 별점: ' + str(SL[1]) + '점')

        aggreF()

    elif n == 3:
        cursor = cnx.cursor()
        priceH = ("select product_name, product_price from product "
                  "where product_price = (select max(product_price) from product)")
        cursor.execute(priceH)
        for PH in cursor:
            print('음식명: ' + PH[0] + ' 가격: ' + str(PH[1]) + '원')

        aggreF()

    elif n == 4:
        cursor = cnx.cursor()
        priceL = ("select product_name, product_price from product "
                  "where product_price = (select min(product_price) from product)")
        cursor.execute(priceL)
        for PL in cursor:
            print('음식명: ' + PL[0] + ' 가격: ' + str(PL[1]) + '원')

        aggreF()

    elif n == 5:
        print('2.1) 종료합니다')
        main()
    else:
        print("잘못입력하신거 같습니다 다시입력해주세요")
        aggreF()


def return_value_F():
    print()
    print('2.2) Define a function which returns a value')
    print('1. 전체 주문 현황 보기')
    print('2. 알밥 판매량 보기')
    print('3. 돈가스 판매량 보기')
    print('4. 자장면 판매량 보기')
    print('5. 종료')
    RVF = int(input())
    if RVF == 1:
        cursor = cnx.cursor()
        AllOrder = ("select * from Orders")
        cursor.execute(AllOrder)
        for AO in cursor:
            print('주문번호: ' + str(AO[0]) + '\n' +
                  '주문시각: ' + str(AO[1]) + ' 배송지주소: ' + AO[2] + ' 주문자 번호: ' + str(AO[3])
                  + ' 요청사항: ' + AO[4] + ' 주문 제품명: ' + AO[5] + ' 제품가격: ' + str(AO[7])+ '원'
                  + ' 제품수량: ' + str(AO[6]) + '개' + ' 총합: ' + str(AO[8]) + '원')

        return_value_F()
    elif RVF == 2:
        cursor = cnx.cursor()
        AlbabO = ("select product_name, product_quantity, total_delivery_amount from Orders"
                  " where product_name = 'Albab'")
        cursor.execute(AlbabO)
        for ALO in cursor:
            print(ALO[0] + ' 총 주문 수량: ' + str(ALO[1]) + '개 ' + '총 판매금액: ' + str(ALO[2]) + '원')
        return_value_F()
    elif RVF == 3:
        cursor = cnx.cursor()
        PCO = ("select product_name, product_quantity, total_delivery_amount from Orders"
                  " where product_name = 'Pork cutlet'")
        cursor.execute(PCO)
        for PorkO in cursor:
            print(PorkO[0] + ' 총 주문 수량: ' + str(PorkO[1]) + '개 ' + '총 판매금액: ' + str(PorkO[2]) + '원')
        return_value_F()
    elif RVF == 4:
        cursor = cnx.cursor()
        JajangO = ("select product_name, product_quantity, total_delivery_amount from Orders"
                  " where product_name = 'jajangmyeon'")
        cursor.execute(JajangO)
        for JJO in cursor:
            print(JJO[0] + ' 총 주문 수량: ' + str(JJO[1]) + '개 ' + '총 판매금액: ' + str(JJO[2]) + '원')
        return_value_F()
    elif RVF == 5:
        print('2.1)을 종료합니다')
        main()
    else:
        print('잘못입력하신거 같습니다 다시입력해주세요')
        return_value_F()


if __name__ == '__main__':
    main()

cnx.close()
