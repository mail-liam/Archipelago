from . import AVTestBase


class TestOptionProgCoatOff(AVTestBase):
    options = {
        "progressive_coat": 0,
    }

    def test_prog_coat_off(self):
        prog_items = self.get_items_by_name(("Progressive Coat",))
        self.assertListEqual(prog_items, [])

        base_items = self.get_items_by_name(("Modified Lab Coat", "Trenchcoat", "Red Coat"))
        self.assertListEqual([item.name for item in base_items], ["Modified Lab Coat", "Trenchcoat", "Red Coat"])


class TestOptionProgCoatOn(AVTestBase):
    options = {
        "progressive_coat": 1,
    }

    def test_prog_coat_on(self):
        base_items = self.get_items_by_name(("Modified Lab Coat", "Trenchcoat", "Red Coat"))
        self.assertListEqual(base_items, [])

        prog_items = self.get_items_by_name(("Progressive Coat",))
        self.assertEqual(len(prog_items), 3)


class TestOptionProgCoatOff(AVTestBase):
    options = {
        "progressive_address_disruptor": 0,
    }

    def test_prog_disruptor_off(self):
        prog_items = self.get_items_by_name(("Progressive Address Disruptor",))
        self.assertListEqual(prog_items, [])

        base_items = self.get_items_by_name(("Address Disruptor 1", "Address Disruptor 2"))
        self.assertListEqual([item.name for item in base_items], ["Address Disruptor 1", "Address Disruptor 2"])


class TestOptionProgDisruptorOn(AVTestBase):
    options = {
        "progressive_address_disruptor": 1,
    }

    def test_prog_disruptor_on(self):
        base_items = self.get_items_by_name(("Address Disruptor 1", "Address Disruptor 2"))
        self.assertListEqual(base_items, [])

        prog_items = self.get_items_by_name(("Progressive Address Disruptor",))
        self.assertEqual(len(prog_items), 2)
