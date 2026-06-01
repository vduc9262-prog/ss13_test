car_park = [
    {'id': 1,
      'name_car':'xe may',
       'name_human': 'nguyen van a'
     },
      {'id': 2,
      'name_car': 'o to ',
       'name_human': 'tran van b'
     },
]

id = 0

while True:
    choice = int(input("""
=================================================
      Quản lý bãi xe - smart parking 
=================================================
    1. thêm mới 
    2.hiển thị 
    3.tìm kiếm 
    4.xóa xe 
    5. thoát 
    mời bạn nhập lựa chọn: """))

    if choice == 1:
        id +=1
        while True:
            new_name_car = input('nhập loại xe mới: ')
            if new_name_car == "":
                print("ko dc nhap trống !")
            else:
                break 
        while True:
            new_name_human = input('nhập tên chủ xe: ')
            if new_name_human == "":
                print("ko dc nhap trống !")
            else:
                break
        new_car = {'id': id, 'name_car': new_name_car, 'name_human': new_name_human }

        car_park.append(new_car)
        print('đã thêm thành công !')

        
        
    elif choice == 2:
        print('ID | loại xe| |chủ xe ')

        for i,p in enumerate(car_park):
            print(f'{p['id']} | {p['name_car']} | {p["name_human"]}  ')
        if car_park == []:
            print("Bãi xe hiện đang trống!")
    

    elif choice == 3:
        for p in car_park:
            search_id = int(input('nhập id cần tìm: '))
            if search_id == p['id']:
                print(f'id: {p['id']}, type:{p['name_car']}, owner: {p['name_human']}')
                break
            else:
                print(f"Không tìm thấy xe có ID {p['id']}!")


    elif choice == 4:
        found = False
        for i,p in enumerate(car_park):
            delete_id = int(input('nhập id cần tìm: '))
            if delete_id == p['id']:
                car_park.pop(i)
                found = True
                print(f' “Đã xóa xe ID {p['id']} thành công!”')
                break
        if not found:
            print("Không tìm thấy xe để xóa!")
    
    elif choice == 5:
        print("thoát chương trình ! ")
        break

    else: 
        print("lỗi cú pháp ! vui lòng nhập lại ")
        
