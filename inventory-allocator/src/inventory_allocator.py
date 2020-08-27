from collections import defaultdict


class InventoryAllocator:
    def __init__(self, all_warehouse_details):
        self.all_warehouse_details = all_warehouse_details
        self.pre_process_warehouse_item_details()  # change names of items in the inventory to lowercase alphabets

    def pre_process_warehouse_item_details(self):
        for warehouse_details in self.all_warehouse_details:
            items_in_warehouse = warehouse_details['inventory']

            for item_name, quantity in items_in_warehouse.items():
                if item_name.lower() == item_name:
                    pass
                else:
                    items_in_warehouse.pop(item_name)
                    items_in_warehouse[item_name.lower()] = quantity

    def get_efficient_way_to_fulfil_order(self, order_details):
        efficient_way_to_fetch_order_items_dict = defaultdict(dict)

        for item_name, quantity in order_details.items():
            if quantity < 0:
                return []

            item = item_name.lower()
            remaining_quantity = quantity

            for warehouse_details in self.all_warehouse_details:
                warehouse_name = warehouse_details['name']
                items_in_warehouse = warehouse_details['inventory']

                if item in items_in_warehouse:
                    quantity_of_item_in_warehouse = items_in_warehouse[item]
                    quantity_needed_from_warehouse = min(remaining_quantity, quantity_of_item_in_warehouse)
                    remaining_quantity -= quantity_of_item_in_warehouse
                    efficient_way_to_fetch_order_items_dict[warehouse_name][item_name] = quantity_needed_from_warehouse

                if remaining_quantity <= 0:
                    break

            if remaining_quantity > 0:
                return []

        return efficient_way_to_fetch_order_items_dict
