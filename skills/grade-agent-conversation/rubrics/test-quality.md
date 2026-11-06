# Test quality

Whether the tests the agent added or edited match the testing rule for this repo, or sit at the wrong layer, repeat another test, or assert nothing.

A score below 0.5 is a failure. Use `not_applicable` when the session does not add or edit a test and the task did not call for one. `not_applicable` is not a failure.

| Label | Score | When to use it |
| --- | --- | --- |
| `tests_match_the_rule` | 1 | The tests check the behavior the task named, at the layer the repo's rule asks for. |
| `small_gap` | 0.8 | One test is thin or slightly off layer, and the rest match the rule. |
| `wrong_layer_or_repeated` | 0.4 | The agent added a set of tests at the wrong layer, such as many unit tests where the rule prefers an end-to-end test, or it repeated a test that already exists. |
| `tests_do_not_check_the_behavior` | 0.2 | The new tests have no real assertion, they pass on a stub, or they lock in the wrong behavior. |

Holmes's fail example was an auth service covered in unit tests where the guideline prefers end-to-end tests. That case is `wrong_layer_or_repeated` unless the tests also fail to assert anything.
