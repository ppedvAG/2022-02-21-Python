import unittest

import Classes.test_Person
import test_helper
import test_modul11

# suite = unittest.TestSuite()
# suite.addTest(test_helper.Test("test_subtract"))
# suite.addTests()
# runner = unittest.TextTestRunner()
# runner.run(suite)
# runner = unittest.TextTestRunner()
# # suiteHelper = unittest.makeSuite(test_helper.Test)
# # suiteModul11 = unittest.makeSuite(test_modul11.test_sum)
# runner.run(suiteHelper)
# runner.run(suiteModul11)

suiteList = [unittest.TestLoader().loadTestsFromTestCase(test_helper.Test),
             unittest.TestLoader().loadTestsFromTestCase(test_modul11.test_sum),
             unittest.TestLoader().loadTestsFromTestCase(Classes.test_Person.TestMyClass)]
comboSuite = unittest.TestSuite(suiteList)

log_file = "test_log.log"
with open(log_file, "w") as f:
    unittest.TextTestRunner(f, verbosity=2).run(comboSuite)

# https://docs.pytest.org/en/7.0.x/
