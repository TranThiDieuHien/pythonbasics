# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:19:18 2020

@author: Trần Thị Diệu Hiền
"""

#Câu 1
#1.Các hàm cơ bản của thư viện os để thao tác với tập tin và thư mục
#os.getcwd() : Trả về thư mục làm việc hiện tại của một tiến trình
#os.listdir() : liệt kê tất cả các tệp, thư mục của đường dẫn được truyền vào
#os.walk() : Trả về danh sách toàn bộ các tập tin, thư mục con trong thư mục làm việc hiện tại và tất cả thư mục con của thư mục hiện tại, bắt đầu từ ()
#os.chdir() : Cho phép bạn thay đổi thư mục làm việc hiện tại sang đường dẫn được truyền vào.
#os.mkdir() : Tạo thư mục
#os.rmdir() : Xóa thư mục
#os.path.join() : Cho phép nối các đường dẫn với nhau theo để tạo nên 1 đường dẫn hoàn chỉnh và phù hợp nhất
#os.makedirs("dir1/dir2") : Tạo thư mục theo đường dẫn được truyền vào
#shutil.copy2("source_file", "destination") hoặc shutil.move("source_file", "destination") : Di chuyển file từ thư mục này sang thư mục khác
#os.remove("my_file_path") : Xóa file ở đường dẫn được truyền vào

import os
#Câu 2
for (root,dirs,files) in os.walk('C:\\'):
    print("Thư mục gốc và thư mục trong ổ đĩa C:",root)
    print("Các thư mục con từ các thư mục gốc",dirs)
    print("Các tập tin từ thư mục gốc và thư mục",files)
    print('--------------------------------')
    
#Câu 3    
path ='C:\\'
list1=list()
list2=list()
for (root,dirs,files) in os.walk(path):  
    for f in files:
        list1.append(f)
    for d in dirs:
        list2.append(d)
print("Danh sách tập tin là:",list1) #Dòng này em dùng để ktra xem tập tin đã được thêm vào list1 chưa
print("Danh sách thư mục con là:",list2) ##Dòng này em dùng để ktra xem thư mục con đã được thêm vào list2 chưa

    
    