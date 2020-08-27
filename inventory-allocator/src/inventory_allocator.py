from collections import defaultdict


class InventoryAllocator:
    def __init__(self, all_warehouse_details):
        self.all_warehouse_details = all_warehouse_details

    def get_efficient_way_to_fulfil_order(self, order_details):
        efficient_way_to_fetch_order_items_dict = defaultdict(dict)

        for item, quantity in order_details.items():
            remaining_quantity = quantity

            for warehouse_details in self.all_warehouse_details:
                warehouse_name = warehouse_details['name']
                items_in_warehouse = warehouse_details['inventory']

                if item in items_in_warehouse:
                    quantity_of_item_in_warehouse = items_in_warehouse[item]
                    quantity_needed_from_warehouse = min(remaining_quantity, quantity_of_item_in_warehouse)
                    remaining_quantity -= quantity_of_item_in_warehouse
                    efficient_way_to_fetch_order_items_dict[warehouse_name][item] = quantity_needed_from_warehouse

                if remaining_quantity <= 0:
                    break

            if remaining_quantity > 0:
                return []

        return efficient_way_to_fetch_order_items_dict


warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}}, {"name": "dm", "inventory": {"banana": 5, "orange": 10}}]
orders = {"apple": 5, "banana": 5, "orange": 5}

ia = InventoryAllocator(warehouses)
print(ia.get_efficient_way_to_fulfil_order(orders))
