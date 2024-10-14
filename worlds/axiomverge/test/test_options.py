from . import AVTestBase


class TestOptionProgCoatOff(AVTestBase):
    options = {
        "progressive_coat": 0,
    }

    def test_prog_coat_off(self):
        prog_coats = self.get_items_by_name(("Progressive Coat",))
        self.assertListEqual(prog_coats, [])

        base_coats = self.get_items_by_name(("Modified Lab Coat", "Trenchcoat", "Red Coat"))
        self.assertListEqual([coat.name for coat in base_coats], ["Modified Lab Coat", "Trenchcoat", "Red Coat"])


class TestOptionProgCoatOn(AVTestBase):
    options = {
        "progressive_coat": 1,
    }

    def test_prog_coat_on(self):
        base_coats = self.get_items_by_name(("Modified Lab Coat", "Trenchcoat", "Red Coat"))
        self.assertListEqual(base_coats, [])

        prog_coats = self.get_items_by_name(("Progressive Coat",))
        self.assertEqual(len(prog_coats), 3)
