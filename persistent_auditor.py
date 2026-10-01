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
    
    def get_valid_input():
    
    product_title = input("Enter Product Name: ")

    if product_title.lower() == "quit":
        return "quit"

    qty_raw = input("Enter Quantity: ")

    if qty_raw.lower() == "quit":
        return "quit"

    if not qty_raw.isdigit():
        
        print("Error: Invalid input. Quantity must be a valid non-negative integer.")
        
        return None

    item_qty = int(qty_raw)

    if item_qty < 0:
        
        print("Error: Negative values are not allowed.")
        
        return None

    return (product_title, item_qty)


def process_delivery(running_total, value_to_add):
    
    return running_total + value_to_add