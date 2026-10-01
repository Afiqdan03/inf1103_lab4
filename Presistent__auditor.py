import os


def load_inventory():
    
    root_path = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(root_path, "orders.txt")
    
    order_list = []
    
    try:
        with open(file_path, "r") as data_file:
            
            for row in data_file:
                
                row_str = row.strip()
                
                if not row_str:
                    continue
                
                segments = [seg.strip() for seg in row_str.split(",")]
                
                if len(segments) >= 3:
                    
                    try:
                        order_num = int(segments[0])
                        
                        product_title = segments[1]
                        
                        item_qty = int(segments[2])
                        
                        order_list.append((order_num, product_title, item_qty))
                        
                    except ValueError:
                        continue
                        
        if order_list:
            
            print("Current Orders:\n")
            
            for o_id, prod_name, amount in order_list:
                
                print(f"{o_id}, {prod_name}, {amount}")
                
            print()
            
        return order_list
        
    except FileNotFoundError:
        
        with open(file_path, "w") as data_file:
            pass
            
        return order_list
        
    except (ValueError, IndexError):
        return order_list
    