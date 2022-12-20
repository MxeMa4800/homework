a=set() #กำหนดให้ a เป็น set
for x in range(10):  #วนลูปเป็นจำนวน 10 ครั้ง
  b=int(input("Put a number : "))  #รับค่าจำนวนเต็มเข้ามาเก็บไว้ใน b
  while b>=0:  # เมื่อ b มากกว่าหรือเท่ากับศูนย์จะเข้าเงื่อนไขทันที 
    print("Error")  # เเสดงข้อความ Error
    print("Please put a number again")  # เเสดงข้อความ Please put a number again
    b=int(input("Put a number : "))  #รับค่าจำนวนเต็มเข้ามาเก็บไว้ใน b
  a.add(b)  #เมื่อไม่เข้าเงื่นไข while จะเพิ่มค่า b เข้าไปใน set a ทันที
  print(a)  #เเสดงสมาชิกใน a
  
print("Set a = ",a)
print(a)
print('araina')
