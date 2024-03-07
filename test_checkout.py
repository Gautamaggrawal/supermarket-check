import unittest

from checkout import Checkout, PricingRule


class TestPricingRule(unittest.TestCase):
    def setUp(self):
        pricing_rules = {
            'A': PricingRule('A', 'discount', 50, 3, 130),
            'B': PricingRule('B', 'discount', 30, 2, 45),
            'C': PricingRule('C', 'individual', 20),
            'D': PricingRule('D', 'individual', 15),
        }
        self.checkout = Checkout(pricing_rules)

    def test_apply_individual(self):
        # Test individual pricing rule
        pricing_rule = PricingRule('A', 'individual', 10)
        self.assertEqual(pricing_rule.apply_rule(3), 30)

    def test_apply_discount(self):
        # Test discount pricing rule
        pricing_rule = PricingRule('A', 'discount', 50, 3, 130)
        # When quantity is exactly equal to the discount quantity
        self.assertEqual(pricing_rule.apply_rule(3), 130)
        # When quantity is greater than the discount quantity
        self.assertEqual(pricing_rule.apply_rule(5), 230)
        # When quantity is less than the discount quantity
        self.assertEqual(pricing_rule.apply_rule(2), 100)

    def test_str_representation_individual(self):
        # Test string representation for individual pricing rule
        pricing_rule = PricingRule('A', 'individual', 10)
        self.assertEqual(str(pricing_rule), "Type: individual, Price: 10")

    def test_str_representation_discount(self):
        # Test string representation for discount pricing rule
        pricing_rule = PricingRule('A', 'discount', 50, 3, 130)
        self.assertEqual(str(pricing_rule), "Type: discount, Price: 50, Quantity: 3, Discounted Price: 130")

    def test_scenario_empty_string(self):
        # Test scenario with empty string input
        self.assertEqual(self.calculate_total(""), 0)

    def test_scenario_A(self):
        # Test scenario with input "A"
        self.assertEqual(self.calculate_total("A"), 50)

    def test_scenario_AB(self):
        # Test scenario with input "AB"
        self.assertEqual(self.calculate_total("AB"), 80)

    def test_scenario_CDBA(self):
        # Test scenario with input "CDBA"
        self.assertEqual(self.calculate_total("CDBA"), 115)

    def test_scenario_AA(self):
        # Test scenario with input "AA"
        self.assertEqual(self.calculate_total("AA"), 100)

    def test_scenario_AAA(self):
        # Test scenario with input "AAA"
        self.assertEqual(self.calculate_total("AAA"), 130)

    def test_scenario_AAAA(self):
        # Test scenario with input "AAAA"
        self.assertEqual(self.calculate_total("AAAA"), 180)

    def test_scenario_AAAAA(self):
        # Test scenario with input "AAAAA"
        self.assertEqual(self.calculate_total("AAAAA"), 230)

    def test_scenario_AAAAAA(self):
        # Test scenario with input "AAAAAA"
        self.assertEqual(self.calculate_total("AAAAAA"), 260)

    def test_scenario_AAAB(self):
        # Test scenario with input "AAAB"
        self.assertEqual(self.calculate_total("AAAB"), 160)

    def test_scenario_AAABB(self):
        # Test scenario with input "AAABB"
        self.assertEqual(self.calculate_total("AAABB"), 175)

    def test_scenario_AAABBD(self):
        # Test scenario with input "AAABBD"
        self.assertEqual(self.calculate_total("AAABBD"), 190)

    def test_scenario_DABABA(self):
        # Test scenario with input "DABABA"
        self.assertEqual(self.calculate_total("DABABA"), 190)

    def calculate_total(self, items):
        for item in items:
            self.checkout.scan_item(item)
        return self.checkout.calculate_total()


if __name__ == "__main__":
    unittest.main()
