import unittest
from inventory_allocator import InventoryAllocator


class MyTestCase(unittest.TestCase):
    def test_fetch_single_item_from_single_warehouse(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5}}]
        orders = {"apple": 5}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = {'owd': {'apple': 5}}
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_fetch_many_items_from_single_warehouse(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}}]
        orders = {"apple": 5, "orange": 10}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = {'owd': {'apple': 5, "orange": 10}}
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_fetch_single_items_from_multiple_warehouses(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        orders = {"apple": 7}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = {'owd': {'apple': 5}, 'dm': {'apple': 2}}
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_fetch_many_items_from_multiple_warehouses(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}}, {"name": "dm", "inventory": {"banana": 5, "orange": 10}}]
        orders = {"apple": 5, "banana": 5, "orange": 5}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = {'owd': {'apple': 5, 'orange': 5}, 'dm': {'banana': 5}}
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_order_item_quantity_exceeds_inventory(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5}}]
        orders = {"apple": 10}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = []
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_order_items_not_in_inventory(self):
        warehouses = [{"name": "owd", "inventory": {"orange": 5}}]
        orders = {"apple": 10}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = []
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_negative_quantity_in_order(self):
        warehouses = [{"name": "owd", "inventory": {"apple": 5}}]
        orders = {"apple": -5}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = []
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)

    def test_item_name_case_mismatch(self):
        warehouses = [{"name": "owd", "inventory": {"aPPLe": 5}}]
        orders = {"ApplE": 5}
        inventory_allocator_object = InventoryAllocator(warehouses)
        expected_res = {'owd': {'ApplE': 5}}
        res = inventory_allocator_object.get_efficient_way_to_fulfil_order(orders)
        self.assertEqual(res, expected_res)


if __name__ == '__main__':
    unittest.main()
