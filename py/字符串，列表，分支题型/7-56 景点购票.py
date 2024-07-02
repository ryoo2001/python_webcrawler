price = int(input())
identity = input()
if identity == "学生":
    fprice = price * 0.8
    print(f"请支付{fprice:.2f}元现金购买一张门票")
else:
    print(f"请支付{price:.2f}元现金购买一张门票")
