from ai_engine.memory.conversation_memory import ConversationMemory
from ai_engine.core.orchestrator import handle_message
from ai_engine.evaluation.test_cases import TEST_CASES

def run():
    passed = 0
    for case in TEST_CASES:
        memory = ConversationMemory()
        result = handle_message(memory, case["input"])

        risk_ok = result["risk_level"] >= case["expected_max_risk"] - 1
        override_ok = (result["safety_action"] == "crisis_response") == case["expect_override"]

        ok = risk_ok and override_ok
        passed += ok

        status = "PASS" if ok else "FAIL"
        print(f"[{status}] '{case['input'][:50]}...' -> risk={result['risk_level']} action={result['safety_action']}")

    print(f"\n{passed}/{len(TEST_CASES)} passed")

if __name__ == "__main__":
    run()
