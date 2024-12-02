from . import AVTestBase
from .. import conditions

class TestCanDamage(AVTestBase):
    def test_can_damage(self):
        state, context = self.multiworld.state, self.multiworld.worlds[1].context
        self.assertFalse(conditions.can_damage(state, context))

        self.collect_by_name(("Kilver",))
        self.assertTrue(conditions.can_damage(state, context))
